"""
Example configuration file for Video Downloader
Copy this file to config_local.py and customize as needed
"""

# Default output directory
DEFAULT_OUTPUT_DIR = "./downloads"

# Default quality
DEFAULT_QUALITY = "best"  # Options: best, high, medium, low

# Default audio format
DEFAULT_AUDIO_FORMAT = "mp3"  # Options: mp3, m4a, wav, aac

# YouTube options
YOUTUBE_OPTIONS = {
    "quiet": False,
    "no_warnings": False,
    "progress": True,
}

# TikTok options
TIKTOK_OPTIONS = {
    "remove_watermark": True,
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
}

# Quality presets - customize as needed
QUALITY_PRESETS = {
    "best": {
        "youtube": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "description": "Best available quality (usually 1080p or 4K)"
    },
    "high": {
        "youtube": "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "description": "Up to 1080p"
    },
    "medium": {
        "youtube": "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "description": "720p quality"
    },
    "low": {
        "youtube": "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "description": "480p or lower"
    }
}

# Timeout settings (in seconds)
REQUEST_TIMEOUT = 30
DOWNLOAD_TIMEOUT = 300  # 5 minutes

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# Logging
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "downloader.log"
