"""Configuration settings for video downloader"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Config:
    """Configuration for video downloaders"""
    
    # Quality presets for different platforms
    QUALITY_PRESETS = {
        "best": {
            "youtube": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "tiktok": "best"
        },
        "high": {
            "youtube": "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "tiktok": "high"
        },
        "medium": {
            "youtube": "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "tiktok": "medium"
        },
        "low": {
            "youtube": "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "tiktok": "low"
        }
    }
    
    # YouTube options
    YOUTUBE_DEFAULT_FORMAT = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
    YOUTUBE_AUDIO_FORMAT = "bestaudio[ext=m4a]"
    
    # TikTok options
    TIKTOK_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    # Supported audio formats
    AUDIO_FORMATS = {
        "mp3": "mp3",
        "m4a": "m4a",
        "wav": "wav",
        "aac": "aac"
    }
    
    # Output template
    OUTPUT_TEMPLATE = "%(title)s.%(ext)s"
    
    @classmethod
    def get_format(cls, platform: str, quality: str) -> str:
        """Get format string based on platform and quality"""
        if quality in cls.QUALITY_PRESETS:
            return cls.QUALITY_PRESETS[quality].get(platform, "best")
        return "best"
