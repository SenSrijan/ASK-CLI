# ASK CLI 🤖

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-orange.svg)](https://github.com/astral-sh/uv)
[![Gemini](https://img.shields.io/badge/Google-Gemini%202.5-4285F4.svg)](https://ai.google.dev/)
[![Groq](https://img.shields.io/badge/Groq-API-FF6B35.svg)](https://groq.com/)
[![Rich](https://img.shields.io/badge/Rich-Terminal%20UI-purple.svg)](https://rich.readthedocs.io/)

**🚀 AI-powered command line Q&A tool with intelligent web search integration**

Get instant, structured answers to any question directly in your terminal. ASK CLI combines the power of Google Gemini and Groq APIs with DuckDuckGo search to deliver comprehensive, well-formatted responses with source attribution.

## ✨ Features

- 🔍 **Smart Web Search** - DuckDuckGo integration for real-time information
- 🧠 **Dual AI Models** - Google Gemini 2.5 Flash Lite (default) + Groq support
- 📊 **Structured Output** - TL;DR, Explanation, Key Points, Sources format
- 🎨 **Beautiful Terminal UI** - Colorful, readable output with Rich formatting
- ⚡ **Lightning Fast** - Optimized for 3-7 second response times
- 🔧 **Highly Configurable** - Custom models, providers, and behavior settings
- 📱 **Multiple Formats** - Terminal markdown or JSON for automation
- 🔒 **Privacy Focused** - Uses DuckDuckGo for web searches
- 🌐 **Cross Platform** - Windows, macOS, Linux support

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **UV Package Manager** ([Install UV](https://docs.astral.sh/uv/getting-started/installation/))
- **API Keys**: [Google Gemini](https://ai.google.dev/) and/or [Groq](https://groq.com/)

### Installation

```bash
# Clone the repository
git clone https://github.com/SenSrijan/ASK-CLI.git
cd ASK-CLI

# Install dependencies
uv sync

# Run installation script
uv run python install.py
```

### Setup API Keys

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file with your API keys:**
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Get API Keys:**
   - **Gemini**: [Google AI Studio](https://ai.google.dev/)
   - **Groq**: [Groq Console](https://console.groq.com/)

## 💻 Usage

### Basic Commands

```bash
# Basic Q&A with web search (default: Gemini)
uv run python -m askcli.cli "Explain LOPA with practical examples"

# Use specific AI provider
uv run python -m askcli.cli "What is Python?" --gemini
uv run python -m askcli.cli "Latest AI trends" --groq

# LLM-only mode (no web search)
uv run python -m askcli.cli "Explain asyncio.gather" --no-web

# Limit search results
uv run python -m askcli.cli "RBI repo rate update" -n 3

# JSON output for automation
uv run python -m askcli.cli "What is Docker?" --json

# Debug mode
uv run python -m askcli.cli "SIS safety systems" --debug
```

### Using Wrapper Scripts

**Windows:**
```cmd
# PowerShell
powershell -ExecutionPolicy Bypass -File ask.ps1 "Your question"

# Batch
ask.bat "Your question"
```

**Linux/macOS:**
```bash
# Make executable
chmod +x ask.sh

# Run
./ask.sh "Your question"
```

## ⚙️ Configuration

### Optional Config File

Create `~/.askcli/config.toml` for custom settings:

```toml
[search]
provider = "duckduckgo"
num_results = 4

[llm]
provider = "gemini"  # or "groq"
model = "gemini-2.5-flash-lite"
max_context_tokens = 8000

[behavior]
use_web_by_default = true
timeout_seconds = 20
cache_enabled = true
```

### CLI Options

| Option | Description | Example |
|--------|-------------|----------|
| `--gemini` | Use Google Gemini (default) | `--gemini` |
| `--groq` | Use Groq API | `--groq` |
| `--no-web` | Skip web search, LLM only | `--no-web` |
| `-n, --num-results` | Limit search results | `-n 3` |
| `--json` | Output in JSON format | `--json` |
| `--debug` | Show debug information | `--debug` |
| `--help` | Show help message | `--help` |

## 📊 Output Format

ASK CLI provides structured, easy-to-read responses:

```
┌─────────────────── >> TL;DR << ───────────────────┐
│ • Key point 1                                     │
│ • Key point 2                                     │
│ • Key point 3                                     │
└───────────────────────────────────────────────────┘

┌─────────────── >> Explanation << ─────────────────┐
│ Detailed explanation of the topic...              │
└───────────────────────────────────────────────────┘

┌──────────────── >> Key Points << ─────────────────┐
│ • Detailed point 1                                │
│ • Detailed point 2                                │
└───────────────────────────────────────────────────┘

┌────────────────── >> Sources << ──────────────────┐
│ 1. Source URL 1                                   │
│ 2. Source URL 2                                   │
└───────────────────────────────────────────────────┘
```

## 🛠 Development

### Project Structure

```
askcli/
├── askcli/                 # Main package
│   ├── cli.py             # CLI interface (Typer)
│   ├── config.py          # Configuration management
│   ├── models.py          # Pydantic data models
│   ├── prompts.py         # LLM prompt templates
│   ├── answer.py          # Main orchestration logic
│   ├── fetcher.py         # Web content extraction
│   ├── search/            # Search providers
│   │   ├── base.py        # Search provider interface
│   │   └── duckduckgo.py  # DuckDuckGo implementation
│   └── llm/               # LLM clients
│       ├── base.py        # LLM client interface
│       ├── groq_client.py # Groq implementation
│       └── gemini_client.py # Gemini implementation
├── tests/                 # Test files
├── docs/                  # Documentation
├── scripts/               # Utility scripts
├── pyproject.toml         # Dependencies & packaging
└── README.md              # This file
```

### Tech Stack

- **Language**: Python 3.11+
- **Package Manager**: UV (modern, fast Python package manager)
- **CLI Framework**: Typer (modern CLI with type hints)
- **HTTP Client**: httpx (async-capable HTTP client)
- **Content Extraction**: trafilatura (clean text from web pages)
- **LLM Integration**: Google Generative AI SDK, Groq SDK
- **Search**: ddgs (DuckDuckGo search)
- **Terminal UI**: Rich (beautiful terminal output)
- **Data Models**: Pydantic (type-safe data structures)
- **Configuration**: TOML + python-dotenv

### Running Tests

```bash
# Setup verification
uv run python test_setup.py

# Demo with mock data
uv run python demo.py

# Installation check
uv run python install.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini](https://ai.google.dev/) for powerful AI capabilities
- [Groq](https://groq.com/) for fast inference
- [DuckDuckGo](https://duckduckgo.com/) for privacy-focused search
- [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- [UV](https://github.com/astral-sh/uv) for modern Python package management

## 📞 Support

If you have any questions or run into issues:

- 🐛 [Report bugs](https://github.com/SenSrijan/ASK-CLI/issues)
- 💡 [Request features](https://github.com/SenSrijan/ASK-CLI/issues)
- 📖 [Check documentation](https://github.com/SenSrijan/ASK-CLI)

---

**⭐ Star this repository if ASK CLI helps you!**