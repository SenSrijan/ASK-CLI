# ASK CLI

A CLI tool for intelligent Q&A with web search capabilities.

## Installation

1. Clone this repository
2. Install with UV:
   ```bash
   uv sync
   ```

## Setup

1. Set your API keys in `.env` file:
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY and/or GROQ_API_KEY
   ```
   
   Or set as environment variables:
   ```bash
   set GEMINI_API_KEY=your_gemini_api_key_here
   set GROQ_API_KEY=your_groq_api_key_here
   ```

2. (Optional) Create config file at `~/.askcli/config.toml`:
   ```toml
   [search]
   provider = "duckduckgo"
   num_results = 4

   [llm]
   provider = "gemini"
   model = "gemini-2.5-flash-lite"
   max_context_tokens = 8000

   [behavior]
   use_web_by_default = true
   timeout_seconds = 20
   cache_enabled = true
   ```

## Usage

### Basic usage with web search:
```bash
uv run python -m askcli.cli ask "Explain LOPA with a practical example"
```

### LLM-only mode (no web search):
```bash
uv run python -m askcli.cli "Explain asyncio.gather with examples" --no-web
```

### Use specific LLM provider:
```bash
# Use Gemini (default)
uv run python -m askcli.cli "What is LOPA?" --gemini

# Use Groq
uv run python -m askcli.cli "What is LOPA?" --groq
```

### Limit search results:
```bash
uv run python -m askcli.cli "Latest RBI repo rate update" -n 3
```

### JSON output:
```bash
uv run python -m askcli.cli "What is LOPA?" --json
```

### Debug mode:
```bash
uv run python -m askcli.cli "What is SIS in safety systems?" --debug
```

## Features

- **Web Search Integration**: Uses DuckDuckGo to find relevant information
- **LLM Processing**: Powered by Google Gemini (default) or Groq's Llama models
- **Structured Output**: TL;DR, Explanation, Key Points, and Sources
- **Configurable**: Customize search providers, models, and behavior
- **Multiple Output Formats**: Terminal-friendly markdown or JSON

## Project Structure

```
askcli/
├── askcli/
│   ├── __init__.py
│   ├── cli.py            # CLI interface
│   ├── config.py         # Configuration management
│   ├── models.py         # Data models
│   ├── prompts.py        # LLM prompt templates
│   ├── answer.py         # Main orchestration logic
│   ├── fetcher.py        # Web content extraction
│   ├── search/
│   │   ├── __init__.py
│   │   ├── base.py       # Search provider interface
│   │   └── duckduckgo.py # DuckDuckGo implementation
│   └── llm/
│       ├── __init__.py
│       ├── base.py       # LLM client interface
│       └── groq_client.py# Groq implementation
├── pyproject.toml
└── README.md
```