#!/usr/bin/env python3
"""Test script to verify ASK CLI setup."""

import sys
import os
from pathlib import Path

# Add the askcli package to path
sys.path.insert(0, str(Path(__file__).parent))

from askcli.config import load_config
from askcli.models import Settings, SearchResult, PageContent
from askcli.search.duckduckgo import DuckDuckGoProvider
from askcli.prompts import build_user_prompt, SYSTEM_PROMPT

def test_config():
    """Test configuration loading."""
    print("Testing configuration loading...")
    try:
        config = load_config()
        print(f"[OK] Config loaded: LLM={config.llm.provider}, Search={config.search.provider}")
        return True
    except Exception as e:
        print(f"[ERROR] Config error: {e}")
        return False

def test_models():
    """Test Pydantic models."""
    print("\nTesting data models...")
    try:
        # Test SearchResult
        result = SearchResult(title="Test", url="https://example.com", snippet="Test snippet")
        print(f"[OK] SearchResult: {result.title}")
        
        # Test PageContent
        content = PageContent(url="https://example.com", title="Test", text="Test content")
        print(f"[OK] PageContent: {content.title}")
        
        # Test Settings
        settings = Settings()
        print(f"[OK] Settings: {settings.llm.model}")
        return True
    except Exception as e:
        print(f"[ERROR] Models error: {e}")
        return False

def test_search():
    """Test search functionality (without API calls)."""
    print("\nTesting search provider...")
    try:
        provider = DuckDuckGoProvider()
        print("[OK] DuckDuckGo provider initialized")
        return True
    except Exception as e:
        print(f"[ERROR] Search error: {e}")
        return False

def test_prompts():
    """Test prompt building."""
    print("\nTesting prompt system...")
    try:
        # Test with no web content
        prompt = build_user_prompt("What is Python?", [])
        print("[OK] No-web prompt built")
        
        # Test with web content
        pages = [PageContent(url="https://example.com", title="Python Info", text="Python is a programming language")]
        prompt = build_user_prompt("What is Python?", pages)
        print("[OK] Web-enabled prompt built")
        
        print(f"[OK] System prompt length: {len(SYSTEM_PROMPT)} chars")
        return True
    except Exception as e:
        print(f"[ERROR] Prompts error: {e}")
        return False

def main():
    """Run all tests."""
    print("ASK CLI Setup Verification")
    print("=" * 30)
    
    tests = [
        test_config,
        test_models,
        test_search,
        test_prompts,
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nResults: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("\n[SUCCESS] ASK CLI is properly set up!")
        print("\nTo use the CLI:")
        print("1. Set GROQ_API_KEY environment variable")
        print("2. Run: uv run python -m askcli.cli \"Your question here\"")
    else:
        print("\n[FAILED] Some tests failed. Check the errors above.")

if __name__ == "__main__":
    main()