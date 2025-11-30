#!/bin/bash
# ASK CLI Bash wrapper script

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

uv run python -m askcli.cli "$@"