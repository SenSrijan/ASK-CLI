from typing import Protocol


class LLMClient(Protocol):
    def answer(self, system: str, user: str) -> str:
        ...