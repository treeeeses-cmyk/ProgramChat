from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict
import uvicorn
from agent import ProgramChatAgent
from config import HOST, PORT, DEBUG

# Инициализируем FastAPI приложение
app = FastAPI(
    title="ProgramChat",
    description="Универсальный AI-агент на базе OpenRouter",
    version="1.0.0"
)

# Создаём экземпляр агента
try:
    agent = ProgramChatAgent()
except ValueError as e:
    print(f"❌ Ошибка инициализации: {e}")
    print("⚠️  Убедитесь, что вы добавили OPENROUTER_API_KEY в .env файл")
    agent = None

# Модели для запросов/ответов
class ChatMessage(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    history_length: int

class HistoryResponse(BaseModel):
    history: List[Dict]
    total_messages: int

# Routes
@app.get("/")
async def root():
    """Проверка статуса сервера"""
    return {
        "status": "✅ ProgramChat запущен!",
        "name": "ProgramChat",
        "version": "1.0.0",
        "description": "Универсальный AI-агент с характером 😎"
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatMessage):
    """Отправить сообщение AI"""
    if not agent:
        raise HTTPException(
            status_code=500,
            detail="Агент не инициализирован. Проверьте OPENROUTER_API_KEY в .env"
        )
    
    if not request.message or not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Сообщение не может быть пустым"
        )
    
    try:
        response = agent.chat(request.message)
        return ChatResponse(
            response=response,
            history_length=len(agent.get_history())
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка при обработке сообщения: {str(e)}"
        )

@app.get("/history", response_model=HistoryResponse)
async def get_history():
    """Получить историю разговоров"""
    if not agent:
        raise HTTPException(
            status_code=500,
            detail="Агент не инициализирован"
        )
    
    history = agent.get_history()
    return HistoryResponse(
        history=history,
        total_messages=len(history)
    )

@app.delete("/history")
async def clear_history():
    """Очистить историю разговоров"""
    if not agent:
        raise HTTPException(
            status_code=500,
            detail="Агент не инициализирован"
        )
    
    agent.clear_history()
    return {"status": "✅ История очищена"}

@app.get("/docs")
async def docs():
    """Документация API"""
    return {
        "message": "Откройте http://localhost:8000/docs для интерактивной документации"
    }

# Обработка ошибок
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": f"Произошла ошибка: {str(exc)}"}
    )

if __name__ == "__main__":
    print("🚀 Запуск ProgramChat...")
    print(f"📡 Сервер доступен на http://{HOST}:{PORT}")
    print(f"📖 Документация на http://{HOST}:{PORT}/docs")
    uvicorn.run(app, host=HOST, port=PORT, reload=DEBUG)
