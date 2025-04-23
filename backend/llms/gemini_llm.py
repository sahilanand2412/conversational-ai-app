from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
from backend.llms.base import BaseLLM

# ✅ Explicitly pass API key from environment
api_key = os.getenv("Google_API_KEY")
if not api_key:
    raise ValueError("❌ Google_API_KEY not found in environment!")

genai.configure(api_key=api_key)

class GeminiLLM(BaseLLM):
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")  # or gemini-2.0-flash
        self.chat = self.model.start_chat(history=[])

    async def call(self, message: str, session_id: str) -> str:
        response = self.chat.send_message(message)
        return response.text
