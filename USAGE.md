# ASK CLI Usage Guide

## Running from Anywhere

### Windows

#### Option 1: PowerShell Script
```powershell
# Add to PATH or run directly
powershell -ExecutionPolicy Bypass -File "D:\Projects\ASK CLI\askcli\ask.ps1" "Your question"
```

#### Option 2: Batch Script
```cmd
# Add to PATH or run directly
"D:\Projects\ASK CLI\askcli\ask.bat" "Your question"
```

#### Option 3: Add to PATH
1. Add `D:\Projects\ASK CLI\askcli` to your PATH environment variable
2. Run from anywhere:
```cmd
ask.bat "Your question"
```

### Linux/macOS

#### Make script executable and add to PATH
```bash
chmod +x "D:\Projects\ASK CLI\askcli\ask.sh"
# Add directory to PATH in ~/.bashrc or ~/.zshrc
export PATH="$PATH:/path/to/askcli"
```

Then run from anywhere:
```bash
ask.sh "Your question"
```

## Examples

```bash
# Basic usage
ask.bat "Explain LOPA with examples"

# No web search
ask.bat "What is Python?" --no-web

# JSON output
ask.bat "Latest AI trends" --json

# Debug mode
ask.bat "What is SIS?" --debug

# Limit results
ask.bat "RBI repo rate" -n 3
```