from backend.utils.config import get_llm

async def get_agent_response(message: str, session_id: str, model: str):
    llm = get_llm(model)
    return await llm.call(message, session_id)
