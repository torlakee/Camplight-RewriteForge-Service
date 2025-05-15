import os
from adapters.openai import OpenAIAdapter
from adapters.gemini import GeminiAdapter
from deployment.read_secrets import read_llm_keys_from_secrets

def provide_llm(provider: str = None):
    """
    Provides an instance of an LLM adapter (OpenAI or Gemini) using the first available API key
    from the .secrets file.

    If no provider is explicitly passed, the function defaults to the environment variable
    `LLM_PROVIDER` or falls back to 'openai'.

    Args:
        provider (str, optional): The name of the LLM provider ('openai' or 'gemini').

    Returns:
        LLMAdapter: An instance of the specified LLM adapter initialized with the first API key.

    Raises:
        ValueError: If no keys are found for the selected provider, or if the provider is unsupported.
    """
    if provider is None:
        provider = os.getenv("LLM_PROVIDER", "openai")

    secrets = read_llm_keys_from_secrets(".secrets")
    keys = secrets.get(provider.lower())

    if not keys:
        raise ValueError(f"No keys found for provider '{provider}' in .secrets")

    sorted_keys = [keys[k] for k in sorted(keys.keys())]

    return get_adapter_for_provider(provider.lower(), sorted_keys[0])

def get_adapter_for_provider(provider: str, api_key: str):
    """
    Returns the appropriate adapter class for the given provider.

    Args:
        provider (str): The provider name ('openai' or 'gemini').
        api_key (str): The API key to initialize the adapter with.

    Returns:
        LLMAdapter: A specific adapter instance matching the provider.

    Raises:
        ValueError: If an unsupported provider is requested.
    """
    if provider == "openai":
        return OpenAIAdapter(api_key=api_key)
    elif provider == "gemini":
        return GeminiAdapter(api_key=api_key)
    else:
        raise ValueError(f"Unsupported provider: {provider}")