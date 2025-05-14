import os
from openai import OpenAIAdapter
from adapter import StubAdapter
from gemini import GeminiAdapter

def provide_llm():
    provider = os.getenv("LLM_PROVIDER", "stub")
    if provider == "openai":
        return OpenAIAdapter()
    elif provider == "gemini":
        return GeminiAdapter()
    return StubAdapter()
