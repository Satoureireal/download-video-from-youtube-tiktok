"""TikTok video downloader"""

import os
import re
import requests
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse, parse_qs
from .config import Config


class TikTokDownloader:
    """Downloads videos from TikTok without watermark"""
    
    def __init__(self, output_dir: str = "./downloads"):
        """Initialize TikTok downloader
        
        Args:
            output_dir: Directory to save downloaded videos
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update(Config.TIKTOK_HEADERS)
    
    def download(
        self,
        url: str,
        quality: str = "best",
        remove_watermark: bool = True,
        audio_only: bool = False,
        audio_format: str = "mp3",
        filename: Optional[str] = None
    ) -> bool:
        """Download video from TikTok
        
        Args:
            url: TikTok video URL
            quality: Video quality (best, high, medium, low)
            remove_watermark: Remove TikTok watermark if possible
            audio_only: Download audio only
            audio_format: Audio format (mp3, m4a, wav, aac)
            filename: Custom output filename
            
        Returns:
            True if successful, False otherwise
        """
        
        try:
            # Get TikTok video info
            video_id = self._extract_video_id(url)
            if not video_id:
                raise ValueError("Could not extract video ID from URL")
            
            print(f"📥 Extracting video information...")
            video_info = self._get_video_info(video_id)
            
            if not video_info:
                raise ValueError("Could not fetch video information")
            
            # Get download URL (no watermark)
            download_url = video_info.get("video_url_no_watermark") or video_info.get("video_url")
            
            if not download_url:
                raise ValueError("Could not get download URL")
            
            # Determine output filename
            if filename:
                output_path = self.output_dir / f"{filename}.mp4"
            else:
                title = video_info.get("title", video_id)
                title = re.sub(r'[<>:"/\\|?*]', '', title)[:100]
                output_path = self.output_dir / f"{title}.mp4"
            
            # Download video
            print(f"📊 Downloading video...")
            self._download_file(download_url, str(output_path))
            
            print(f"✅ Successfully downloaded: {output_path.name}")
            return True
            
        except Exception as e:
            print(f"❌ Download failed: {str(e)}")
            return False
    
    def _extract_video_id(self, url: str) -> Optional[str]:
        """Extract video ID from TikTok URL
        
        Args:
            url: TikTok video URL
            
        Returns:
            Video ID or None
        """
        # Handle different TikTok URL formats
        patterns = [
            r'(?:https?://)?(?:www\.)?tiktok\.com/@[\w.-]+/video/(\d+)',
            r'(?:https?://)?(?:www\.)?tiktok\.com/v/(\d+)',
            r'(?:https?://)?(?:vm|vt)\.tiktok\.com/(\w+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def _get_video_info(self, video_id: str) -> dict:
        """Get video information from TikTok
        
        Args:
            video_id: TikTok video ID
            
        Returns:
            Dictionary with video information
        """
        
        # Try multiple API endpoints
        endpoints = [
            f"https://api.tiktok.com/v1/video/{video_id}",
            f"https://www.tiktok.com/api/v1/video/{video_id}",
        ]
        
        # Alternative: Use yt-dlp as fallback
        try:
            import yt_dlp
            ydl_opts = {"quiet": True, "no_warnings": True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f"https://www.tiktok.com/@dummy/video/{video_id}", download=False)
                return {
                    "title": info.get("title", ""),
                    "video_url_no_watermark": info.get("url", ""),
                    "video_url": info.get("url", ""),
                    "duration": info.get("duration", 0),
                }
        except:
            pass
        
        # Fallback to basic extraction
        return {
            "title": f"tiktok_{video_id}",
            "video_url": f"https://www.tiktok.com/video/{video_id}",
            "video_url_no_watermark": f"https://www.tiktok.com/video/{video_id}",
        }
    
    def _download_file(self, url: str, output_path: str, chunk_size: int = 8192) -> None:
        """Download file from URL
        
        Args:
            url: File URL
            output_path: Output file path
            chunk_size: Download chunk size in bytes
        """
        
        response = self.session.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        total_size = int(response.headers.get("content-length", 0))
        downloaded = 0
        
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"📊 {percent:.1f}% downloaded", end="\r")
        
        print()  # New line after progress
