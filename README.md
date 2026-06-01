# 🎬 Video Downloader - YouTube & TikTok

A powerful tool to download videos from YouTube and TikTok with high quality, without watermarks, and with multiple format options.

## ✨ Features

- **🎥 Multiple Platforms**: Download from YouTube and TikTok
- **📊 High Quality**: Support for best, high, medium, and low quality options
- **🚫 No Watermarks**: Removes TikTok watermarks (when possible)
- **🎵 Audio Extraction**: Download audio only in MP3, M4A, WAV, or AAC format
- **🎛️ Format Options**: Customizable video and audio formats
- **📁 Flexible Output**: Custom filenames and output directories
- **🖥️ GUI & CLI**: Both graphical and command-line interfaces available

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- FFmpeg (required for audio conversion)

### Step 1: Clone or Download

```bash
git clone <repository-url>
cd "download video from youtube tiktok"
```

### Step 2: Install FFmpeg

**Windows (using Chocolatey):**
```powershell
choco install ffmpeg
```

**Windows (Manual):**
1. Download from https://ffmpeg.org/download.html
2. Extract and add to PATH

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 📖 Usage

### Method 1: GUI Application (Recommended for beginners)

```bash
python gui.py
```

A user-friendly interface will open where you can:
- Enter video URL
- Select platform (auto-detect or manual)
- Choose quality and format
- Set output directory
- View download progress and logs

### Method 2: Command Line Interface

#### Basic YouTube download (best quality):
```bash
python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

#### Download TikTok without watermark:
```bash
python main.py -u "https://www.tiktok.com/@username/video/1234567890" -wm
```

#### Download audio only (MP3):
```bash
python main.py -u "URL" -a --audio-format mp3
```

#### Custom quality and format:
```bash
python main.py -u "URL" -q high -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
```

#### Save with custom filename:
```bash
python main.py -u "URL" -n "my-video" -o "./my-downloads"
```

### CLI Arguments

| Argument | Short | Description | Options |
|----------|-------|-------------|---------|
| `--url` | `-u` | Video URL (required) | YouTube or TikTok URL |
| `--platform` | `-p` | Video platform | `youtube`, `tiktok`, `auto` |
| `--quality` | `-q` | Video quality | `best`, `high`, `medium`, `low` |
| `--format` | `-f` | Custom format string | yt-dlp format specification |
| `--audio-only` | `-a` | Download audio only | Flag (no value) |
| `--remove-watermark` | `-wm` | Remove watermark | Flag (only for TikTok) |
| `--output` | `-o` | Output directory | Path (default: `./downloads`) |
| `--name` | `-n` | Custom filename | String (without extension) |
| `--audio-format` | | Audio format | `mp3`, `m4a`, `wav`, `aac` |

## 📋 Examples

### YouTube Examples

```bash
# Download best quality video
python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download 720p MP4
python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -q high

# Download audio only
python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -a

# Custom format (1080p or 720p MP4)
python main.py -u "URL" -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
```

### TikTok Examples

```bash
# Download without watermark
python main.py -u "https://www.tiktok.com/@username/video/1234567890" -p tiktok -wm

# Download audio only
python main.py -u "https://www.tiktok.com/@username/video/1234567890" -a --audio-format mp3

# Save to custom location with custom name
python main.py -u "https://www.tiktok.com/@username/video/1234567890" -o "./tiktoks" -n "viral_video"
```

## 🎯 Quality Options

### YouTube
- **Best** (default): Highest available quality (usually 1080p or 4K)
- **High**: Up to 1080p
- **Medium**: Up to 720p
- **Low**: Up to 480p

### TikTok
- **Best**: Highest available quality
- **High**: High quality
- **Medium**: Medium quality
- **Low**: Low quality

## 📁 File Structure

```
download video from youtube tiktok/
├── main.py                          # CLI entry point
├── gui.py                          # GUI application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── downloader/
    ├── __init__.py                # Package initialization
    ├── config.py                  # Configuration settings
    ├── youtube_downloader.py      # YouTube downloader
    └── tiktok_downloader.py       # TikTok downloader
```

## 🔧 Troubleshooting

### Issue: "yt-dlp not found"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: "FFmpeg not found"
**Solution**: Install FFmpeg (see Installation section)

### Issue: Download fails with 403 error
**Solution**: The video might be restricted. Try:
- Using a VPN
- Checking if the URL is correct
- Waiting a few hours before retrying

### Issue: TikTok watermark not removed
**Solution**: This is expected if TikTok blocks the API. The tool will still download the video with watermark.

### Issue: No audio in downloaded video
**Solution**: Ensure FFmpeg is properly installed and in PATH. You can verify:
```bash
ffmpeg -version
```

## ⚠️ Legal Notice

This tool is for **personal use only**. Respect copyright and intellectual property rights:
- Only download content you have permission to download
- Do not redistribute downloaded content without permission
- Check local laws regarding video downloading

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

This project is provided as-is for educational purposes.

## 🙋 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the Examples section
3. Check if the URL format is correct

## 🎓 Technical Details

### Technologies Used
- **yt-dlp**: YouTube/TikTok downloading and format handling
- **requests**: HTTP requests for file downloads
- **FFmpeg**: Audio/video processing and conversion
- **tkinter**: Cross-platform GUI toolkit (built-in with Python)

### Supported Formats

**Video Formats**: MP4, MKV, WebM, etc.
**Audio Formats**: MP3, M4A, WAV, AAC

### Platform Support
- ✅ Windows
- ✅ macOS
- ✅ Linux

---

**Made with ❤️ for video enthusiasts**
