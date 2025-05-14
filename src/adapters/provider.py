import os
from adapters.openai import OpenAIAdapter
from adapters.gemini import GeminiAdapter
from deployment.read_secrets import read_llm_keys_from_secrets

def provide_llm(provider: str = None):
    if provider is None:
        provider = os.getenv("LLM_PROVIDER", "openai")

    secrets = read_llm_keys_from_secrets(".secrets")
    keys = secrets.get(provider.lower())

    if not keys:
        raise ValueError(f"No keys found for provider '{provider}' in .secrets")

    sorted_keys = [keys[k] for k in sorted(keys.keys())]

def get_adapter_for_provider(provider: str, api_key: str):
    if provider == "openai":
        return OpenAIAdapter(api_key=api_key)
    elif provider == "gemini":
        return GeminiAdapter(api_key=api_key)
    else:
        raise ValueError(f"Unsupported provider: {provider}")