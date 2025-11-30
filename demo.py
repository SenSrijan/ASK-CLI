#!/usr/bin/env python3
"""Demo script showing ASK CLI functionality with mock responses."""

import sys
from pathlib import Path

# Add the askcli package to path
sys.path.insert(0, str(Path(__file__).parent))

from askcli.models import SearchResult, PageContent
from askcli.prompts import build_user_prompt, SYSTEM_PROMPT
from askcli.fetcher import gather_context
from rich.console import Console
from rich.markdown import Markdown

def mock_search_results():
    """Generate mock search results for demonstration."""
    return [
        SearchResult(
            title="LOPA - Layer of Protection Analysis",
            url="https://example.com/lopa-guide",
            snippet="LOPA is a semi-quantitative risk assessment methodology used in process safety..."
        ),
        SearchResult(
            title="Practical LOPA Implementation",
            url="https://example.com/lopa-practical",
            snippet="Step-by-step guide to implementing LOPA in industrial settings..."
        ),
        SearchResult(
            title="LOPA Case Studies",
            url="https://example.com/lopa-cases",
            snippet="Real-world examples of LOPA application in chemical plants..."
        )
    ]

def mock_page_content():
    """Generate mock page content for demonstration."""
    return [
        PageContent(
            url="https://example.com/lopa-guide",
            title="LOPA - Layer of Protection Analysis",
            text="""LOPA (Layer of Protection Analysis) is a semi-quantitative risk assessment methodology 
            used in process safety management. It evaluates the adequacy of protection layers against 
            potential hazardous scenarios. LOPA helps determine if existing safeguards are sufficient 
            or if additional protection layers are needed. The methodology considers initiating events, 
            independent protection layers (IPLs), and consequence severity to calculate risk levels."""
        ),
        PageContent(
            url="https://example.com/lopa-practical",
            title="Practical LOPA Implementation",
            text="""A practical LOPA study involves: 1) Identifying hazardous scenarios from HAZOP studies,
            2) Defining initiating event frequencies, 3) Identifying independent protection layers,
            4) Calculating scenario risk, 5) Comparing against risk tolerance criteria. For example,
            in a reactor overpressure scenario: Initiating event = control system failure (1E-1/year),
            IPL1 = pressure relief valve (PFD=1E-2), IPL2 = high pressure alarm (PFD=1E-1).
            Scenario frequency = 1E-1 × 1E-2 × 1E-1 = 1E-4/year."""
        )
    ]

def mock_llm_response():
    """Generate mock LLM response for demonstration."""
    return """## TL;DR

• LOPA is a semi-quantitative risk assessment method for process safety
• Evaluates protection layers against hazardous scenarios using frequency analysis
• Helps determine if additional safeguards are needed beyond existing protection
• Widely used in chemical and process industries for risk management

## Explanation

Layer of Protection Analysis (LOPA) is a structured methodology used to evaluate the adequacy of protection layers in process safety management. It bridges the gap between qualitative hazard identification (like HAZOP) and full quantitative risk assessment (QRA).

LOPA works by analyzing specific hazardous scenarios identified during hazard studies. For each scenario, it considers the initiating event frequency and the effectiveness of independent protection layers (IPLs) to calculate the overall scenario risk frequency.

## Key Points

• **Semi-quantitative approach**: Uses order-of-magnitude estimates rather than precise calculations
• **Independent Protection Layers**: Only counts safeguards that are truly independent and reliable
• **Risk tolerance criteria**: Compares calculated risk against acceptable risk levels
• **Practical decision-making**: Helps determine cost-effective risk reduction measures
• **Industry standard**: Widely accepted in chemical, oil & gas, and pharmaceutical industries

## Sources

1. [LOPA - Layer of Protection Analysis](https://example.com/lopa-guide)
2. [Practical LOPA Implementation](https://example.com/lopa-practical)
3. [LOPA Case Studies](https://example.com/lopa-cases)"""

def demo_prompt_building():
    """Demonstrate prompt building functionality."""
    console = Console()
    
    console.print("[bold blue]ASK CLI Demo - Prompt Building[/bold blue]")
    console.print("=" * 50)
    
    query = "Explain LOPA with a practical example"
    console.print(f"\n[bold green]Query:[/bold green] {query}")
    
    # Demo 1: No web content
    console.print("\n[bold yellow]1. LLM-only mode (--no-web):[/bold yellow]")
    prompt_no_web = build_user_prompt(query, [])
    console.print(f"Prompt length: {len(prompt_no_web)} characters")
    
    # Demo 2: With web content
    console.print("\n[bold yellow]2. Web-enabled mode:[/bold yellow]")
    pages = mock_page_content()
    prompt_with_web = build_user_prompt(query, pages)
    console.print(f"Prompt length: {len(prompt_with_web)} characters")
    console.print(f"Web sources: {len(pages)} pages")
    
    return prompt_with_web

def demo_output_formatting():
    """Demonstrate output formatting."""
    console = Console()
    
    console.print("\n[bold blue]ASK CLI Demo - Output Formatting[/bold blue]")
    console.print("=" * 50)
    
    # Show mock LLM response formatted as markdown
    response = mock_llm_response()
    md = Markdown(response)
    console.print(md)

def main():
    """Run the demo."""
    console = Console()
    
    console.print("[bold magenta]ASK CLI Demonstration[/bold magenta]")
    console.print("This demo shows how ASK CLI processes queries and formats responses.")
    console.print("(Using mock data since no API key is configured)\n")
    
    # Demo prompt building
    demo_prompt_building()
    
    # Demo output formatting  
    demo_output_formatting()
    
    console.print("\n[bold green]Demo completed![/bold green]")
    console.print("\nTo use ASK CLI with real data:")
    console.print("1. Set GROQ_API_KEY environment variable")
    console.print("2. Run: uv run python -m askcli.cli \"Your question here\"")

if __name__ == "__main__":
    main()