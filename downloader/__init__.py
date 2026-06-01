"""Downloader package for YouTube and TikTok videos"""

__version__ = "1.0.0"
__author__ = "Video Downloader Tool"

from .youtube_downloader import YouTubeDownloader
from .tiktok_downloader import TikTokDownloader
from .config import Config

__all__ = [
    "YouTubeDownloader",
    "TikTokDownloader",
    "Config"
]
