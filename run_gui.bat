@echo off
REM GUI startup script for Windows

cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found. Please install Python first.
    echo Download from: https://www.python.org
    pause
    exit /b 1
)

REM Run GUI
python gui.py
