import typer
from typing import Optional
from .answer import handle_query

app = typer.Typer(help="ASK CLI - Intelligent Q&A with web search")


@app.command()
def main(
    query: str = typer.Argument(..., help="Your question"),
    num_results: Optional[int] = typer.Option(None, "--num-results", "-n", help="Number of search results"),
    no_web: bool = typer.Option(False, "--no-web", help="Skip web search, use LLM only"),
    json_output: bool = typer.Option(False, "--json", help="Output in JSON format"),
    debug: bool = typer.Option(False, "--debug", help="Show debug information"),
    gemini: bool = typer.Option(False, "--gemini", help="Use Gemini LLM (default)"),
    groq: bool = typer.Option(False, "--groq", help="Use Groq LLM"),
):
    """Ask a question and get an intelligent answer with sources."""
    from rich.console import Console
    from rich.text import Text
    
    console = Console()
    
    # Determine LLM provider
    llm_provider = None
    if groq:
        llm_provider = "groq"
    elif gemini:
        llm_provider = "gemini"
    # Default to gemini if neither specified
    
    if not json_output:
        # Show colorful header
        header = Text("ASK CLI", style="bold magenta")
        header.append(" | ", style="dim")
        header.append("Intelligent Q&A", style="bold cyan")
        if not no_web:
            header.append(" with web search", style="green")
        
        # Show LLM provider
        provider_name = llm_provider or "gemini"
        header.append(f" [{provider_name.upper()}]", style="bold yellow")
        
        console.print(header)
        console.print()
    
    try:
        response = handle_query(
            query=query,
            num_results=num_results,
            use_web=not no_web,
            debug=debug,
            as_json=json_output,
            llm_provider=llm_provider,
        )
        print(response)
    except Exception as e:
        if debug:
            raise
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()