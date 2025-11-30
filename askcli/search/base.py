from typing import Protocol, List
from ..models import SearchResult


class SearchProvider(Protocol):
    def search(self, query: str, n: int = 5) -> List[SearchResult]:
        ...