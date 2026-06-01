@echo off
REM Web Video Downloader - Windows Startup Script

color 0A
cls

echo ========================================
echo   Video Downloader - Web Version
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found
    echo Please install Python 3.7+
    pause
    exit /b 1
)

REM Check requirements
echo [1/3] Checking dependencies...
python -m pip show flask >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing dependencies...
    python -m pip install -q -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install dependencies
        pause
        exit /b 1
    )
)
echo [OK] Dependencies installed

REM Check FFmpeg
echo [2/3] Checking FFmpeg...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo [WARNING] FFmpeg not found
    echo Please install FFmpeg from https://ffmpeg.org/download.html
    echo Or run: choco install ffmpeg
    echo.
    set /p CONTINUE="Continue anyway? (y/n): "
    if /i not "%CONTINUE%"=="y" exit /b 1
) else (
    echo [OK] FFmpeg found
)

REM Start Flask server
echo [3/3] Starting Flask server...
echo.
echo ========================================
echo Opening browser in 3 seconds...
echo Access the app at: http://localhost:5000
echo ========================================
echo.

timeout /t 3 /nobreak
start http://localhost:5000

python app.py
