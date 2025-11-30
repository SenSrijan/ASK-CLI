import os
from groq import Groq
from .base import LLMClient


class GroqClient:
    def __init__(self, model: str = "qwen/qwen3-32b"):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is required")
        self.client = Groq(api_key=api_key)
        self.model = model

    def answer(self, system: str, user: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ],
            temperature=0.1,
            max_tokens=2000
        )
        return response.choices[0].message.content