from adapters.adapter import LLMAdapter

class StubAdapter(LLMAdapter):
    async def rewrite(self, text: str, style: str) -> str:
        return f"[*{style}*] {text}"
