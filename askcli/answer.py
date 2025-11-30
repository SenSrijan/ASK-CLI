import json
from typing import Optional, List

try:
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.rule import Rule
except ImportError:
    # Fallback for environments where rich is not available
    Console = None
    Markdown = None
    Panel = None
    Table = None
    Text = None
    Rule = None
from .config import load_config
from .llm.groq_client import GroqClient
from .search.duckduckgo import DuckDuckGoProvider
from .fetcher import gather_context
from .prompts import SYSTEM_PROMPT, build_user_prompt
from .models import SearchResult, PageContent


def get_llm_client(config, provider_override=None):
    """Factory function to get LLM client."""
    provider = provider_override or config.llm.provider
    
    if provider == "groq":
        return GroqClient("qwen/qwen3-32b")
    elif provider == "gemini":
        from .llm.gemini_client import GeminiClient
        return GeminiClient("gemini-2.5-flash-lite")
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")


def get_search_provider(config):
    """Factory function to get search provider."""
    if config.search.provider == "duckduckgo":
        return DuckDuckGoProvider()
    else:
        raise ValueError(f"Unknown search provider: {config.search.provider}")


def print_debug_info(search_results: List[SearchResult], pages: List[PageContent]):
    """Print colorful debug information about search and content."""
    console = Console()
    
    # Search results table
    if search_results:
        table = Table(title="[bold magenta]Search Results[/bold magenta]", show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim", width=3)
        table.add_column("Title", style="cyan")
        table.add_column("URL", style="blue", overflow="fold")
        
        for i, result in enumerate(search_results, 1):
            table.add_row(str(i), result.title, result.url)
        
        console.print(table)
    
    # Content pages info
    if pages:
        content_info = "\n".join([f"* {page.title} ({len(page.text)} chars)" for page in pages])
        console.print(Panel(content_info, title="[bold green]Content Extracted[/bold green]", border_style="green"))
    else:
        console.print(Panel("[yellow]No content extracted from web sources[/yellow]", border_style="yellow"))


def answer_to_json(answer_markdown: str, search_results: List[SearchResult]) -> str:
    """Convert answer to JSON format."""
    return json.dumps({
        "answer": answer_markdown,
        "sources": [{"title": r.title, "url": r.url} for r in search_results]
    }, indent=2)


def render_markdown_to_terminal(markdown_text: str) -> str:
    """Render colorful formatted output to terminal."""
    console = Console()
    
    # Parse sections from markdown
    sections = markdown_text.split('## ')
    
    with console.capture() as capture:
        for i, section in enumerate(sections):
            if not section.strip():
                continue
                
            lines = section.strip().split('\n')
            title = lines[0] if lines else ""
            content = '\n'.join(lines[1:]) if len(lines) > 1 else ""
            
            if title == "TL;DR":
                console.print(Panel(content, title="[bold cyan]>> TL;DR <<[/bold cyan]", border_style="cyan", padding=(1, 2)))
            elif title == "Explanation":
                console.print(Panel(content, title="[bold green]>> Explanation <<[/bold green]", border_style="green", padding=(1, 2)))
            elif title == "Key Points":
                console.print(Panel(content, title="[bold yellow]>> Key Points <<[/bold yellow]", border_style="yellow", padding=(1, 2)))
            elif title == "Sources":
                console.print(Panel(content, title="[bold magenta]>> Sources <<[/bold magenta]", border_style="magenta", padding=(1, 2)))
            
            if i < len(sections) - 1:
                console.print()
    
    return capture.get()


def handle_query(
    query: str,
    num_results: Optional[int] = None,
    use_web: bool = True,
    debug: bool = False,
    as_json: bool = False,
    llm_provider: Optional[str] = None
) -> str:
    """Main function to handle a query and return formatted answer."""
    config = load_config()
    llm = get_llm_client(config, llm_provider)
    
    search_results = []
    pages = []
    
    if use_web:
        try:
            provider = get_search_provider(config)
            search_results = provider.search(
                query, 
                n=num_results or config.search.num_results
            )
            pages = gather_context(search_results, max_total_chars=8000)
        except Exception as e:
            if debug:
                print(f"Web search failed, falling back to LLM-only: {e}")
            use_web = False
    
    if debug:
        print_debug_info(search_results, pages)
        console = Console()
        console.print()
    
    user_prompt = build_user_prompt(query, pages)
    answer_markdown = llm.answer(SYSTEM_PROMPT, user_prompt)
    
    if as_json:
        return answer_to_json(answer_markdown, search_results)
    
    return render_markdown_to_terminal(answer_markdown)