@echo off
REM ASK CLI Windows batch wrapper script

cd /d "%~dp0"
uv run python -m askcli.cli %*