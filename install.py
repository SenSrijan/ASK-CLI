#!/usr/bin/env python3
"""Installation script for ASK CLI."""

import os
import sys
import subprocess
from pathlib import Path

def check_uv():
    """Check if UV is installed."""
    try:
        result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] UV found: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass
    
    print("[ERROR] UV package manager not found!")
    print("Install UV from: https://docs.astral.sh/uv/getting-started/installation/")
    return False

def install_dependencies():
    """Install project dependencies."""
    print("\n[INFO] Installing dependencies with UV...")
    try:
        result = subprocess.run(["uv", "sync"], check=True, capture_output=True, text=True)
        print("[OK] Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to install dependencies: {e}")
        return False

def create_config():
    """Create default configuration file."""
    config_dir = Path.home() / ".askcli"
    config_file = config_dir / "config.toml"
    
    if config_file.exists():
        print(f"[INFO] Configuration already exists at {config_file}")
        return True
    
    print(f"[INFO] Creating configuration directory at {config_dir}")
    config_dir.mkdir(exist_ok=True)
    
    config_content = """[search]
provider = "duckduckgo"
num_results = 4

[llm]
provider = "groq"
model = "gemini-2.5-flash-lite"
max_context_tokens = 8000

[behavior]
use_web_by_default = true
timeout_seconds = 20
cache_enabled = true
"""
    
    with open(config_file, 'w') as f:
        f.write(config_content)
    
    print(f"[OK] Configuration created at {config_file}")
    return True

def check_api_key():
    """Check if Groq API key is set."""
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GROQ_API_KEY")
    env_file = Path(".env")
    
    if api_key and api_key != "your_groq_api_key_here":
        print("[OK] GROQ_API_KEY is configured")
        return True
    else:
        print("[WARNING] GROQ_API_KEY not configured")
        if env_file.exists():
            print("Edit .env file and set GROQ_API_KEY=your_actual_key")
        else:
            print("Copy .env.example to .env and set GROQ_API_KEY=your_actual_key")
        return False

def test_installation():
    """Test the installation."""
    print("\n[INFO] Testing installation...")
    try:
        result = subprocess.run([
            "uv", "run", "python", "-m", "askcli.cli", "--help"
        ], capture_output=True, text=True, check=True)
        print("[OK] CLI command works")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] CLI test failed: {e}")
        return False

def main():
    """Main installation function."""
    print("ASK CLI Installation")
    print("=" * 30)
    
    steps = [
        ("Checking UV installation", check_uv),
        ("Installing dependencies", install_dependencies),
        ("Creating configuration", create_config),
        ("Checking API key", check_api_key),
        ("Testing installation", test_installation),
    ]
    
    success_count = 0
    for step_name, step_func in steps:
        print(f"\n{step_name}...")
        if step_func():
            success_count += 1
    
    print(f"\nInstallation completed: {success_count}/{len(steps)} steps successful")
    
    if success_count >= 4:  # API key is optional
        print("\n[SUCCESS] ASK CLI is ready to use!")
        print("\nUsage examples:")
        print('  uv run python -m askcli.cli "What is LOPA?"')
        print('  uv run python -m askcli.cli --no-web "Explain Python lists"')
        print('  uv run python -m askcli.cli --json "Latest AI trends"')
    else:
        print("\n[FAILED] Installation incomplete. Check errors above.")

if __name__ == "__main__":
    main()