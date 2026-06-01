# Quick Start Guide - 🎬 Video Downloader

## 🚀 Quick Installation (Windows)

1. **Double-click** `install.bat` to set up the tool
2. Wait for installation to complete
3. A shortcut "Video Downloader" will appear on your Desktop

## 🎯 Quick Usage

### Using the GUI (Easiest)
```
Click the "Video Downloader" shortcut on Desktop
OR type in terminal: python gui.py
```

### Using Command Line
```bash
# YouTube download
python main.py -u "https://www.youtube.com/watch?v=VIDEO_ID"

# TikTok download without watermark
python main.py -u "https://www.tiktok.com/@user/video/ID" -wm

# Audio only (MP3)
python main.py -u "URL" -a

# Custom folder and filename
python main.py -u "URL" -o "./my_videos" -n "my-video"
```

## 📋 Common Tasks

### Download YouTube Video in Best Quality
```bash
python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```
Output: Video saved to `./downloads/` folder

### Download YouTube Video as MP3 Audio
```bash
python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -a
```
Output: MP3 file in `./downloads/` folder

### Download TikTok Without Watermark
```bash
python main.py -u "https://www.tiktok.com/@username/video/1234567890" -wm
```
Output: Video without TikTok logo

### Download to Custom Location
```bash
python main.py -u "URL" -o "C:/my_videos"
```

### Download with Custom Filename
```bash
python main.py -u "URL" -n "my-awesome-video"
```
Output: `./downloads/my-awesome-video.mp4`

## 🎯 Quality Options

- **best**: Highest quality available (default)
- **high**: Up to 1080p
- **medium**: Up to 720p  
- **low**: Up to 480p

Example:
```bash
python main.py -u "URL" -q high
```

## 🎵 Audio Formats

- **mp3**: Most compatible (default)
- **m4a**: Good quality, smaller size
- **wav**: Lossless audio
- **aac**: High quality

Example:
```bash
python main.py -u "URL" -a --audio-format m4a
```

## 🆘 Troubleshooting

### Error: "python is not recognized"
- **Windows**: Reinstall Python and check "Add Python to PATH"
- **Mac/Linux**: Use `python3` instead of `python`

### Error: "FFmpeg not found"
- **Windows**: Run `choco install ffmpeg` or download from ffmpeg.org
- **Mac**: Run `brew install ffmpeg`
- **Linux**: Run `sudo apt-get install ffmpeg`

### Download fails
- Check if the URL is correct
- Try a different video
- Check your internet connection

## 📁 Where are Downloaded Files?

By default, videos are saved in: `./downloads/` folder in the project directory

You can change this with `-o` option:
```bash
python main.py -u "URL" -o "D:/Videos"
```

## ℹ️ Tips

1. **First time setup**: Run `install.bat` (Windows) or `install.sh` (Mac/Linux)
2. **GUI is easier**: Use `gui.py` for a user-friendly interface
3. **Check URLs**: Make sure to copy the full video URL
4. **File size**: High-quality videos can be large (100MB+)
5. **Patience**: Large videos may take a few minutes to download

## 🎓 All Commands Reference

```bash
python main.py --help
```

This shows all available options with descriptions.

---

**Need more help?** See the full README.md file for detailed documentation.
