#!/bin/bash

# Web Video Downloader - Unix/Mac Startup Script

echo "========================================"
echo "  Video Downloader - Web Version"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 not found"
    echo "Please install Python 3.7+"
    exit 1
fi

echo "[1/3] Checking dependencies..."
pip3 show flask > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "[INFO] Installing dependencies..."
    pip3 install -q -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install dependencies"
        exit 1
    fi
fi
echo "[OK] Dependencies installed"

# Check FFmpeg
echo "[2/3] Checking FFmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "[WARNING] FFmpeg not found"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macOS: brew install ffmpeg"
    else
        echo "Linux: sudo apt-get install ffmpeg"
    fi
    echo ""
    read -p "Continue anyway? (y/n): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "[OK] FFmpeg found"
fi

# Start Flask server
echo "[3/3] Starting Flask server..."
echo ""
echo "========================================"
echo "Access the app at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo ""

# Try to open browser
if [[ "$OSTYPE" == "darwin"* ]]; then
    sleep 2 && open http://localhost:5000 &
else
    sleep 2 && xdg-open http://localhost:5000 2>/dev/null &
fi

python3 app.py
