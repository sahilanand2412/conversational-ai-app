from fastapi import FastAPI
from backend.mcp.router import router as chat_router

app = FastAPI(title="Conversational AI MCP Server")
app.include_router(chat_router, prefix="/chat")

@app.get("/")
def root():
    return {"message": "MCP Server is running"}
