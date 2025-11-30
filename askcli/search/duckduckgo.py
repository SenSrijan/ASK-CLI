from typing import List
from ddgs import DDGS
from ..models import SearchResult
from .base import SearchProvider


class DuckDuckGoProvider:
    def search(self, query: str, n: int = 5) -> List[SearchResult]:
        """Search using DuckDuckGo and return structured results."""
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=n))
                return [
                    SearchResult(
                        title=result.get("title", ""),
                        url=result.get("href", ""),
                        snippet=result.get("body", "")
                    )
                    for result in results
                ]
        except Exception as e:
            print(f"Search failed: {e}")
            return []