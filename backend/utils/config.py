import os
from dotenv import load_dotenv

load_dotenv()

def get_llm(model: str):
    from backend.llms.openai_llm import OpenAILLM
    from backend.llms.gemini_llm import GeminiLLM
    from backend.llms.claude_llm import ClaudeLLM

    if model == "openai":
        return OpenAILLM()
    elif model == "gemini":
        return GeminiLLM()
    elif model == "claude":
        return ClaudeLLM()
    else:
        raise ValueError("Unsupported model")
