class BaseLLM:
    async def call(self, message: str, session_id: str) -> str:
        raise NotImplementedError("LLM call not implemented.")
