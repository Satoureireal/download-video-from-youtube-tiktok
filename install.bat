@echo off
REM Installation script for Windows
echo.
echo ================================================
echo Video Downloader - Setup
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/3] Python found. Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [2/3] Checking FFmpeg installation...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo.
    echo WARNING: FFmpeg not found in PATH
    echo FFmpeg is required for audio conversion
    echo.
    echo Installation instructions:
    echo 1. Download from: https://ffmpeg.org/download.html
    echo 2. Extract to a folder
    echo 3. Add the folder to Windows PATH
    echo.
    echo Or use: choco install ffmpeg (if Chocolatey is installed)
    echo.
    pause
) else (
    echo FFmpeg found. Good!
)

echo.
echo [3/3] Creating shortcuts...

REM Create GUI shortcut
echo Creating GUI shortcut...
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Video Downloader.lnk'); $Shortcut.TargetPath = '%cd%\gui.py'; $Shortcut.WorkingDirectory = '%cd%'; $Shortcut.Save()"

echo.
echo ================================================
echo Installation completed!
echo ================================================
echo.
echo Usage:
echo   GUI version: python gui.py
echo      or click the "Video Downloader" shortcut on Desktop
echo.
echo   CLI version: python main.py -u "URL" -q best
echo.
echo For help: python main.py --help
echo.
pause
