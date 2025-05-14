import os
from adapters.openai import OpenAIAdapter
from adapters.stub import StubAdapter
from adapters.gemini import GeminiAdapter

def provide_llm():
    provider = os.getenv("LLM_PROVIDER", "stub")
    if provider == "openai":
        return OpenAIAdapter()
    elif provider == "gemini":
        return GeminiAdapter()
    return StubAdapter()
