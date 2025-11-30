#!/usr/bin/env pwsh
# ASK CLI PowerShell wrapper script

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $SCRIPT_DIR

uv run python -m askcli.cli @args