@echo off
REM ASK CLI Windows batch wrapper script

setlocal
cd /d "%~dp0"
if errorlevel 1 (
    echo Error: Could not change to script directory
    exit /b 1
)

uv run python -m askcli.cli %*
endlocal