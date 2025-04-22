from fastapi import APIRouter, Request
from pydantic import BaseModel
from backend.mcp.agent import get_agent_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    session_id: str
    model: str = "gemini"  # Default changed to Gemini
 # default

@router.post("/")
async def chat(request: ChatRequest):
    response = await get_agent_response(request.message, request.session_id, request.model)
    return {"response": response}
