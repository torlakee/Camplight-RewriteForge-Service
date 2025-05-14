class LLMAdapter:
    async def rewrite(self, text: str, style: str) -> str:
        raise NotImplementedError
