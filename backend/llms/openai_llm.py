from backend.llms.base import BaseLLM
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAILLM(BaseLLM):
    async def call(self, message: str, session_id: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message["content"]
