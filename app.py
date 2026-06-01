"""
Web Video Downloader - Flask Backend
Downloads videos from YouTube and TikTok without watermarks
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import os
import uuid
import json
from pathlib import Path
import threading
import time
from downloader.youtube_downloader import YouTubeDownloader
from downloader.tiktok_downloader import TikTokDownloader

app = Flask(__name__)
CORS(app)

# Configuration
DOWNLOADS_DIR = Path("./downloads")
DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR = Path("./temp")
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# Store download progress
download_progress = {}


def cleanup_old_files():
    """Cleanup old downloaded files"""
    try:
        for folder in [DOWNLOADS_DIR, TEMP_DIR]:
            for file in folder.glob("*"):
                if file.is_file():
                    try:
                        file.unlink()
                    except:
                        pass
    except:
        pass


@app.route("/")
def index():
    """Serve main page"""
    return render_template("index.html")


@app.route("/api/download", methods=["POST"])
def download():
    """Download video endpoint"""
    try:
        data = request.json
        url = data.get("url", "").strip()
        platform = data.get("platform", "auto")
        quality = data.get("quality", "best")
        audio_only = data.get("audio_only", False)
        audio_format = data.get("audio_format", "mp3")
        remove_watermark = data.get("remove_watermark", True)
        
        if not url:
            return jsonify({"status": "error", "message": "❌ Vui lòng nhập URL"}), 400
        
        # Generate session ID
        session_id = str(uuid.uuid4())
        download_progress[session_id] = {
            "status": "starting",
            "progress": 0,
            "message": "Đang chuẩn bị...",
            "file": None
        }
        
        # Auto-detect platform
        if platform == "auto":
            if "youtube.com" in url or "youtu.be" in url:
                platform = "youtube"
            elif "tiktok.com" in url:
                platform = "tiktok"
            else:
                download_progress[session_id] = {
                    "status": "error",
                    "message": "❌ Không thể xác định nền tảng. Vui lòng chọn thủ công"
                }
                return jsonify(download_progress[session_id]), 400
        
        # Start download in background thread
        thread = threading.Thread(
            target=perform_download,
            args=(session_id, url, platform, quality, audio_only, audio_format, remove_watermark)
        )
        thread.daemon = True
        thread.start()
        
        return jsonify({
            "status": "started",
            "session_id": session_id,
            "message": f"🎬 Bắt đầu tải từ {platform.upper()}..."
        })
    
    except Exception as e:
        return jsonify({"status": "error", "message": f"❌ Lỗi: {str(e)}"}), 500


def perform_download(session_id, url, platform, quality, audio_only, audio_format, remove_watermark):
    """Perform actual download"""
    try:
        download_progress[session_id]["status"] = "downloading"
        download_progress[session_id]["message"] = f"📥 Đang tải xuống {platform.upper()}..."
        
        output_file = None
        
        if platform == "youtube":
            downloader = YouTubeDownloader(str(DOWNLOADS_DIR))
            downloader.download(
                url=url,
                quality=quality,
                audio_only=audio_only,
                audio_format=audio_format
            )
            output_file = "Video đã tải"
        else:  # tiktok
            downloader = TikTokDownloader(str(DOWNLOADS_DIR))
            downloader.download(
                url=url,
                quality=quality,
                remove_watermark=remove_watermark,
                audio_only=audio_only,
                audio_format=audio_format
            )
            output_file = "Video đã tải"
        
        download_progress[session_id] = {
            "status": "completed",
            "progress": 100,
            "message": "✅ Tải xuống thành công!",
            "file": output_file
        }
    
    except Exception as e:
        download_progress[session_id] = {
            "status": "error",
            "message": f"❌ Lỗi: {str(e)}"
        }


@app.route("/api/progress/<session_id>", methods=["GET"])
def get_progress(session_id):
    """Get download progress"""
    if session_id in download_progress:
        return jsonify(download_progress[session_id])
    return jsonify({"status": "error", "message": "Session not found"}), 404


@app.route("/api/status", methods=["GET"])
def get_status():
    """Get API status"""
    return jsonify({
        "status": "ok",
        "message": "Video Downloader API is running",
        "version": "1.0.0"
    })


if __name__ == "__main__":
    cleanup_old_files()
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV", "production") != "production"
    app.run(debug=debug, host="0.0.0.0", port=port)
