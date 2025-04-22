from backend.llms.base import BaseLLM

class ClaudeLLM(BaseLLM):
    async def call(self, message: str, session_id: str) -> str:
        return f"[Claude Stub] You said: {message}"
