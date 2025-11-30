#!/usr/bin/env pwsh
# ASK CLI PowerShell wrapper script

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
Push-Location $SCRIPT_DIR

try {
    uv run python -m askcli.cli @args
} finally {
    Pop-Location
}