#!/bin/bash
# ASK CLI Bash wrapper script

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if uv is available
if ! command -v uv &> /dev/null; then
    echo "Error: UV package manager not found. Please install UV first."
    exit 1
fi

uv run python -m askcli.cli "$@"