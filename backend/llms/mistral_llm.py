from backend.llms.base import BaseLLM

class MistralLLM(BaseLLM):
    async def call(self, message: str, session_id: str) -> str:
        return f"[Mistral Stub] You said: {message}"
