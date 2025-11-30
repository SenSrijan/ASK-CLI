import httpx
import trafilatura
from typing import List
from .models import SearchResult, PageContent


def fetch_page(url: str, timeout: int = 10) -> str:
    """Fetch HTML content from URL."""
    try:
        with httpx.Client() as client:
            response = client.get(url, timeout=timeout, follow_redirects=True)
            response.raise_for_status()
            return response.text
    except Exception:
        return ""


def extract_main_text(html: str) -> str:
    """Extract main text content from HTML."""
    extracted = trafilatura.extract(html)
    return extracted or ""


def get_page_content(result: SearchResult, max_chars: int = 4000) -> PageContent:
    """Get clean text content from a search result."""
    html = fetch_page(result.url)
    if not html:
        return PageContent(url=result.url, title=result.title, text="")
    
    text = extract_main_text(html)[:max_chars]
    return PageContent(url=result.url, title=result.title, text=text)


def gather_context(results: List[SearchResult], max_total_chars: int = 12000) -> List[PageContent]:
    """Gather and combine content from search results."""
    contents = []
    used_chars = 0
    
    for result in results:
        page = get_page_content(result)
        if not page.text:
            continue
        
        if used_chars + len(page.text) > max_total_chars:
            break
            
        contents.append(page)
        used_chars += len(page.text)
    
    return contents