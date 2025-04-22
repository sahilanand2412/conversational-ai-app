import os
import google.generativeai as genai
from backend.llms.base import BaseLLM
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiLLM(BaseLLM):
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        self.chat = self.model.start_chat(history=[])

    async def call(self, message: str, session_id: str) -> str:
        response = self.chat.send_message(message)
        return response.text
