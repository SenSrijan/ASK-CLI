import os
import google.generativeai as genai
from .base import LLMClient


class GeminiClient:
    def __init__(self, model: str = "gemini-2.5-flash-lite"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    def answer(self, system: str, user: str) -> str:
        try:
            prompt = f"{system}\n\n{user}"
            response = self.model.generate_content(prompt)
            if hasattr(response, 'text') and response.text:
                return response.text
            else:
                return "Error: No response generated from Gemini API"
        except Exception as e:
            return f"Error: Gemini API failed - {str(e)}"