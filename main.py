#!/usr/bin/env python3
"""
Video Downloader Tool for YouTube and TikTok
Downloads videos without watermarks in high quality with format options
"""

import os
import sys
import argparse
from pathlib import Path
from downloader.youtube_downloader import YouTubeDownloader
from downloader.tiktok_downloader import TikTokDownloader
from downloader.config import Config


def main():
    parser = argparse.ArgumentParser(
        description="Download videos from YouTube and TikTok without watermarks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download YouTube video in best quality
  python main.py -u "https://www.youtube.com/watch?v=..." -q best
  
  # Download TikTok video without watermark
  python main.py -u "https://www.tiktok.com/@.../video/..." -p tiktok -wm
  
  # Download with custom format
  python main.py -u "URL" -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
  
  # Download audio only
  python main.py -u "URL" -a
        """
    )
    
    parser.add_argument(
        "-u", "--url",
        required=True,
        help="Video URL (YouTube or TikTok)"
    )
    
    parser.add_argument(
        "-p", "--platform",
        choices=["youtube", "tiktok", "auto"],
        default="auto",
        help="Video platform (default: auto-detect)"
    )
    
    parser.add_argument(
        "-q", "--quality",
        choices=["best", "high", "medium", "low"],
        default="best",
        help="Video quality (default: best)"
    )
    
    parser.add_argument(
        "-f", "--format",
        default=None,
        help="Custom format string (overrides quality setting)"
    )
    
    parser.add_argument(
        "-a", "--audio-only",
        action="store_true",
        help="Download audio only (MP3)"
    )
    
    parser.add_argument(
        "-wm", "--remove-watermark",
        action="store_true",
        help="Remove watermark if possible (TikTok)"
    )
    
    parser.add_argument(
        "-o", "--output",
        default="./downloads",
        help="Output directory (default: ./downloads)"
    )
    
    parser.add_argument(
        "-n", "--name",
        default=None,
        help="Custom output filename (without extension)"
    )
    
    parser.add_argument(
        "--audio-format",
        choices=["mp3", "m4a", "wav", "aac"],
        default="mp3",
        help="Audio format (default: mp3)"
    )
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Detect platform if auto
    platform = args.platform
    if platform == "auto":
        if "youtube.com" in args.url or "youtu.be" in args.url:
            platform = "youtube"
        elif "tiktok.com" in args.url:
            platform = "tiktok"
        else:
            print("❌ Error: Could not detect platform. Please specify with -p")
            sys.exit(1)
    
    print(f"🎬 Downloading from {platform.upper()}...")
    
    try:
        if platform == "youtube":
            downloader = YouTubeDownloader(str(output_dir))
            downloader.download(
                url=args.url,
                quality=args.quality,
                audio_only=args.audio_only,
                audio_format=args.audio_format,
                custom_format=args.format,
                filename=args.name
            )
        elif platform == "tiktok":
            downloader = TikTokDownloader(str(output_dir))
            downloader.download(
                url=args.url,
                quality=args.quality,
                remove_watermark=args.remove_watermark,
                audio_only=args.audio_only,
                audio_format=args.audio_format,
                filename=args.name
            )
        
        print(f"✅ Download completed! Video saved in: {output_dir}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
