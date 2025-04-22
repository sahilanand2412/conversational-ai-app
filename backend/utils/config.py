import os
from dotenv import load_dotenv

load_dotenv()

def get_llm(model: str):
    from backend.llms.openai_llm import OpenAILLM
    from backend.llms.gemini_llm import GeminiLLM
    from backend.llms.claude_llm import ClaudeLLM
    from backend.llms.mistral_llm import MistralLLM  # new

    if model == "gemini":
        return GeminiLLM()
    elif model == "openai":
        return OpenAILLM()
    elif model == "claude":
        return ClaudeLLM()
    elif model == "mistral":
        return MistralLLM()
    else:
        raise ValueError("Unsupported model")
