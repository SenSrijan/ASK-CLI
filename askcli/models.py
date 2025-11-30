from pydantic import BaseModel
from typing import Optional


class SearchResult(BaseModel):
    title: str
    url: str
    snippet: Optional[str] = None


class PageContent(BaseModel):
    url: str
    title: str
    text: str


class Settings(BaseModel):
    class SearchConfig(BaseModel):
        provider: str = "duckduckgo"
        num_results: int = 4

    class LLMConfig(BaseModel):
        provider: str = "gemini"
        model: str = "gemini-2.5-flash-lite"
        max_context_tokens: int = 8000

    class BehaviorConfig(BaseModel):
        use_web_by_default: bool = True
        timeout_seconds: int = 20
        cache_enabled: bool = True

    search: SearchConfig = SearchConfig()
    llm: LLMConfig = LLMConfig()
    behavior: BehaviorConfig = BehaviorConfig()