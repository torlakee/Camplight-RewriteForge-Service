from adapters.adapter import LLMAdapter
import google.generativeai as genai
from deployment.prompt_templates import rewrite_prompt
import asyncio

class GeminiAdapter(LLMAdapter):
    def __init__(self, api_key: str):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    async def rewrite(self, text: str, style: str) -> str:
        prompt = rewrite_prompt(text, style)
        return await asyncio.to_thread(self._sync_generate, prompt)

    def _sync_generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text.strip()