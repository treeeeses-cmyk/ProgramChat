# ProgramChat 🎮

**ProgramChat** — это универсальный AI-агент на базе OpenRouter с уникальным характером и харизмой!

> *Агент, который соблазнит твоих игроков и немного их подколет 😎*

## 🚀 Быстрый старт

### 1. Требования
- Python 3.9+
- pip
- API ключ от [OpenRouter.ai](https://openrouter.ai)

### 2. Клонируйте репозиторий
```bash
git clone https://github.com/treeeeses-cmyk/ProgramChat.git
cd ProgramChat
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

### 4. Добавьте ваш API ключ
Создайте файл `.env`:
```env
OPENROUTER_API_KEY=your_api_key_here
```

**Как получить ключ:**
1. Зайдите на [OpenRouter.ai](https://openrouter.ai)
2. Зарегистрируйтесь или войдите
3. Перейдите в раздел API Keys
4. Создайте новый ключ
5. Скопируйте его в `.env` файл

### 5. Запустите приложение
```bash
python main.py
```

🎉 Сервер запустится на `http://localhost:8000`

## 📡 API Endpoints

### 1. Отправить сообщение
**POST** `/chat`
```json
{
  "message": "Привет! Помоги мне с кодом"
}
```

**Ответ:**
```json
{
  "response": "Ну да ты сосали? 😎 Конечно помогу!",
  "history_length": 2
}
```

### 2. Получить историю
**GET** `/history`

**Ответ:**
```json
{
  "history": [
    {"role": "user", "content": "Привет"},
    {"role": "assistant", "content": "Привет! 😎"}
  ],
  "total_messages": 2
}
```

### 3. Очистить историю
**DELETE** `/history`

**Ответ:**
```json
{"status": "✅ История очищена"}
```

### 4. Проверка статуса
**GET** `/`

### 5. Интерактивная документация
**GET** `/docs` - Откройте в браузере для Swagger UI

## 🎯 Особенности ProgramChat

✨ **Универсальный AI-агент** - помогает со всем  
🎭 **Уникальный персонаж** - остроумный и харизматичный  
💬 **История разговоров** - помнит контекст  
🔧 **Интеграция с OpenRouter** - доступ к лучшим моделям  
⚡ **FastAPI** - быстрое и надёжное API  
😎 **Собственный стиль** - соблазняет и подкалывает  

## 📋 Структура проекта

```
ProgramChat/
├── main.py              # FastAPI приложение
├── config.py            # Конфигурация и промпты
├── agent.py             # Логика AI-агента
├── requirements.txt     # Зависимости Python
├── .env.example         # Пример конфигурации
├── .gitignore          # Git ignore правила
└── README.md           # Этот файл
```

## 💡 Примеры использования

### Python
```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={"message": "Как написать функцию на Python?"}
)
print(response.json())
```

### cURL
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Привет!"}'
```

### JavaScript
```javascript
const response = await fetch('http://localhost:8000/chat', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({message: 'Как дела?'})
});
const data = await response.json();
console.log(data.response);
```

## 🔧 Конфигурация

Вы можете изменить:
- **Модель**: измените `MODEL` в `config.py`
- **Системный промпт**: отредактируйте `SYSTEM_PROMPT` в `config.py`
- **Порт**: измените `PORT` в `config.py`
- **Температуру**: отредактируйте `temperature` в `agent.py`

### Популярные модели OpenRouter
- `meta-llama/llama-2-70b-chat` (быстро и хорошо)
- `openai/gpt-3.5-turbo` (мощно и надёжно)
- `openai/gpt-4` (самая сильная)
- `mistralai/mistral-7b-instruct` (лёгкая и быстрая)

## 🐛 Решение проблем

### "OPENROUTER_API_KEY не установлен"
- Создайте файл `.env` в корне проекта
- Добавьте строку: `OPENROUTER_API_KEY=your_key_here`
- Перезагрузите приложение

### "Ошибка при подключении"
- Проверьте интернет соединение
- Убедитесь, что ключ API активен
- Проверьте баланс на OpenRouter.ai

### "Модель не найдена"
- Проверьте имя модели в `config.py`
- Убедитесь, что модель доступна на OpenRouter

## 📚 Документация

- [OpenRouter API Docs](https://openrouter.ai/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Python Requests](https://requests.readthedocs.io/)

## 📄 Лицензия

MIT License - свободно используйте в своих проектах!

## 👨‍💻 Автор

Создано с ❤️ для любителей AI и программирования

---

**Готов к боевым условиям!** 🚀😎
