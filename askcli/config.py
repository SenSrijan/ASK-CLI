import os
import toml
from pathlib import Path
from dotenv import load_dotenv
from .models import Settings


def load_config() -> Settings:
    """Load configuration from file and environment variables."""
    # Load .env file
    load_dotenv()
    
    config_path = os.getenv("ASKCLI_CONFIG")
    if not config_path:
        config_path = Path.home() / ".askcli" / "config.toml"
    
    config_data = {}
    if Path(config_path).exists():
        with open(config_path, 'r') as f:
            config_data = toml.load(f)
    
    # Override with environment variables
    if os.getenv("ASKCLI_LLM_MODEL"):
        config_data.setdefault("llm", {})["model"] = os.getenv("ASKCLI_LLM_MODEL")
    
    if os.getenv("GROQ_API_KEY"):
        config_data.setdefault("llm", {})["groq_api_key"] = os.getenv("GROQ_API_KEY")
    
    if os.getenv("GEMINI_API_KEY"):
        config_data.setdefault("llm", {})["gemini_api_key"] = os.getenv("GEMINI_API_KEY")
    
    return Settings(**config_data)