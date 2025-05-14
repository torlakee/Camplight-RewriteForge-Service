from adapters.adapter import LLMAdapter
from openai import AsyncOpenAI
from deployment.prompt_templates import rewrite_prompt

class OpenAIAdapter(LLMAdapter):
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key)

    async def rewrite(self, text: str, style: str) -> str:
        prompt = rewrite_prompt(text, style)

        response = await self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )

        return response.choices[0].message.content.strip()