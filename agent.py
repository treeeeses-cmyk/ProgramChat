import requests
import json
from config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, MODEL, SYSTEM_PROMPT
from typing import List, Dict, Optional

class ProgramChatAgent:
    def __init__(self):
        self.api_key = OPENROUTER_API_KEY
        self.base_url = OPENROUTER_BASE_URL
        self.model = MODEL
        self.system_prompt = SYSTEM_PROMPT
        self.conversation_history: List[Dict] = []
        
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY не установлен в .env файле")
    
    def add_message(self, role: str, content: str):
        """Добавить сообщение в историю"""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def chat(self, user_message: str) -> str:
        """Отправить сообщение и получить ответ от AI"""
        # Добавляем пользовательское сообщение
        self.add_message("user", user_message)
        
        try:
            # Готовим запрос к OpenRouter
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "HTTP-Referer": "https://github.com/treeeeses-cmyk/ProgramChat",
                "X-Title": "ProgramChat",
                "Content-Type": "application/json"
            }
            
            # Подготавливаем сообщения для API
            messages = [
                {"role": "system", "content": self.system_prompt}
            ] + self.conversation_history
            
            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": 0.8,
                "max_tokens": 1024,
            }
            
            # Отправляем запрос
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            
            # Получаем ответ
            result = response.json()
            
            if "error" in result:
                return f"❌ Ошибка: {result['error'].get('message', 'Неизвестная ошибка')}"
            
            assistant_message = result["choices"][0]["message"]["content"]
            
            # Добавляем ответ в историю
            self.add_message("assistant", assistant_message)
            
            return assistant_message
            
        except requests.exceptions.RequestException as e:
            return f"❌ Ошибка при подключении: {str(e)}"
        except json.JSONDecodeError:
            return "❌ Ошибка при обработке ответа от API"
        except Exception as e:
            return f"❌ Неожиданная ошибка: {str(e)}"
    
    def get_history(self) -> List[Dict]:
        """Получить историю разговора"""
        return self.conversation_history
    
    def clear_history(self):
        """Очистить историю разговора"""
        self.conversation_history = []
    
    def reset(self):
        """Сбросить агента"""
        self.clear_history()
