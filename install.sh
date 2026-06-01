#!/bin/bash

# Installation script for macOS and Linux

echo ""
echo "================================================"
echo "Video Downloader - Setup"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed"
    echo "Please install Python 3.7+ first"
    exit 1
fi

echo "[1/3] Python found. Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo ""
echo "[2/3] Checking FFmpeg installation..."
if ! command -v ffmpeg &> /dev/null; then
    echo ""
    echo "WARNING: FFmpeg not found"
    echo "FFmpeg is required for audio conversion"
    echo ""
    echo "Installation instructions:"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macOS: brew install ffmpeg"
    else
        echo "Linux: sudo apt-get install ffmpeg"
    fi
    
    echo ""
    read -p "Continue? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "FFmpeg found. Good!"
fi

echo ""
echo "[3/3] Setup completed!"
echo ""
echo "================================================"
echo "Installation completed!"
echo "================================================"
echo ""
echo "Usage:"
echo "  GUI version: python3 gui.py"
echo ""
echo "  CLI version: python3 main.py -u \"URL\" -q best"
echo ""
echo "For help: python3 main.py --help"
echo ""

# Make scripts executable
chmod +x gui.py main.py install.sh
