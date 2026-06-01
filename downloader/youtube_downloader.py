"""YouTube video downloader using yt-dlp"""

import yt_dlp
from pathlib import Path
from typing import Optional
from .config import Config


class YouTubeDownloader:
    """Downloads videos from YouTube"""
    
    def __init__(self, output_dir: str = "./downloads"):
        """Initialize YouTube downloader
        
        Args:
            output_dir: Directory to save downloaded videos
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def download(
        self,
        url: str,
        quality: str = "best",
        audio_only: bool = False,
        audio_format: str = "mp3",
        custom_format: Optional[str] = None,
        filename: Optional[str] = None
    ) -> bool:
        """Download video from YouTube
        
        Args:
            url: YouTube video URL
            quality: Video quality (best, high, medium, low)
            audio_only: Download audio only
            audio_format: Audio format (mp3, m4a, wav, aac)
            custom_format: Custom format string (overrides quality)
            filename: Custom output filename
            
        Returns:
            True if successful, False otherwise
        """
        
        # Determine format
        if custom_format:
            format_str = custom_format
        elif audio_only:
            format_str = Config.YOUTUBE_AUDIO_FORMAT
        else:
            format_str = Config.get_format("youtube", quality)
        
        # Build output template
        if filename:
            output_template = str(self.output_dir / filename)
        else:
            output_template = str(self.output_dir / Config.OUTPUT_TEMPLATE)
        
        # Configure yt-dlp
        ydl_opts = {
            "format": format_str,
            "outtmpl": output_template,
            "quiet": False,
            "no_warnings": False,
            "progress_hooks": [self._progress_hook],
        }
        
        # Audio-specific options
        if audio_only:
            ydl_opts.update({
                "extract_audio": True,
                "audio_format": audio_format,
                "audio_quality": "192",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": audio_format,
                    "preferredquality": "192",
                    "nopostprocessor": False,
                }]
            })
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"📥 Downloading: {url}")
                info = ydl.extract_info(url, download=True)
                print(f"✅ Successfully downloaded: {info.get('title', 'Unknown')}")
                return True
                
        except Exception as e:
            print(f"❌ Download failed: {str(e)}")
            return False
    
    @staticmethod
    def _progress_hook(d):
        """Progress hook for download status"""
        if d["status"] == "downloading":
            percent = d.get("_percent_str", "0%")
            speed = d.get("_speed_str", "0 B/s")
            eta = d.get("_eta_str", "unknown")
            print(f"📊 {percent} @ {speed} ETA: {eta}", end="\r")
        elif d["status"] == "finished":
            print(f"\n✅ Download finished, now processing...")
