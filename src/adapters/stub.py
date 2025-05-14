from adapters.llmadapter import BaseLLMAdapter

class StubAdapter(BaseLLMAdapter):
    async def rewrite(self, text: str, style: str) -> str:
        return f"[*{style}*] {text}"
