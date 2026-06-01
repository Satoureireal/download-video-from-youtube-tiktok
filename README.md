# 🎬 Video Downloader - Web Version

A modern, beautiful web application to download videos from YouTube and TikTok with high quality, without watermarks, and with multiple format options.

## ✨ Features

- **🎥 Multiple Platforms**: Download from YouTube and TikTok
- **📊 High Quality**: Support for best, high, medium, and low quality options
- **🚫 No Watermarks**: Removes TikTok watermarks (when possible)
- **🎵 Audio Extraction**: Download audio only in MP3, M4A, WAV, or AAC format
- **🎛️ Format Options**: Customizable video and audio formats
- **🌐 Web Interface**: Beautiful, modern UI with responsive design
- **⚡ Real-time Progress**: Live download progress tracking
- **💻 Cross-Platform**: Works on Windows, macOS, and Linux
- **☁️ Cloud Ready**: Deploy on Railway, Render, or Replit for free

## 🚀 Quick Start

### 🖥️ Run Locally

**Windows:**
```bash
# Double-click run.bat
# OR manually:
pip install -r requirements.txt
python app.py
# Go to http://localhost:5000
```

**macOS/Linux:**
```bash
bash run.sh
```

### ☁️ Deploy Online (Recommended)

**Deploy to Railway.app (Free):**

See [GITHUB-DEPLOY.md](GITHUB-DEPLOY.md) for complete instructions.

Quick steps:
1. Push to GitHub: `git push`
2. Go to https://railway.app
3. Connect GitHub
4. Deploy
5. Get public URL ✅

---

## 📖 Documentation

- **[SETUP.md](SETUP.md)** - Installation guide
- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference
- **[DEPLOY.md](DEPLOY.md)** - Deployment options
- **[GITHUB-DEPLOY.md](GITHUB-DEPLOY.md)** - GitHub & Railway setup

---

## 📁 Project Structure

```
download-video-tool/
├── app.py                      # Flask backend
├── requirements.txt            # Python dependencies
├── Procfile                    # Production config
├── runtime.txt                 # Python version
├── packages.txt                # System packages (FFmpeg)
├── templates/
│   └── index.html             # Web interface
├── static/
│   ├── css/
│   │   └── style.css          # Styling
│   └── js/
│       └── app.js             # Frontend logic
├── downloader/                # Video download modules
│   ├── __init__.py
│   ├── config.py
│   ├── youtube_downloader.py
│   └── tiktok_downloader.py
└── .github/workflows/          # GitHub Actions (CI/CD)
```

---

## 🎯 How to Use

1. **Enter Video URL**: YouTube or TikTok link
2. **Select Platform**: Auto-detect or manual choice
3. **Choose Quality**: Best, High, Medium, or Low
4. **Select Format**: MP3, M4A, WAV, or AAC (for audio)
5. **Check Options**:
   - ☑️ Audio only
   - ☑️ Remove watermark (TikTok)
6. **Click "Tải video"** and wait!

---

## 🛠️ Technology Stack

- **Backend**: Flask + Python
- **Frontend**: HTML5, CSS3, JavaScript
- **Video Processing**: yt-dlp + FFmpeg
- **Hosting**: Railway, Render, or Replit
- **Package Management**: pip

---

## 🌐 Deployment Options

| Platform | Cost | Setup | Performance |
|----------|------|-------|-------------|
| **Railway** ⭐ | $5/month | ⭐⭐⭐ | ⚡⚡⚡ |
| **Render** | Free (limited) | ⭐⭐ | ⚡⚡ |
| **Replit** | Free | ⭐⭐⭐ | ⚡ |

**Recommended**: Railway.app (best balance of cost and performance)

## 📖 How to Use

1. **Paste URL**: Paste your YouTube or TikTok video URL
2. **Choose Platform**: Auto-detect or select manually
3. **Select Quality**: Best, High, Medium, or Low
4. **Set Options**: 
   - Audio only (download as MP3, M4A, WAV, or AAC)
   - Remove watermark (for TikTok)
5. **Download**: Click "Tải video" and wait for completion

## 🎯 Quality Options

### YouTube
- **🔥 Best**: Highest available quality (usually 1080p or 4K)
- **⭐ High**: Up to 1080p
- **📺 Medium**: Up to 720p
- **💾 Low**: Up to 480p

### TikTok
- All quality levels supported
- Watermark removal available

## 📁 File Structure

```
download video from youtube tiktok/
├── app.py                          # Flask backend
├── run.bat                         # Windows startup (double-click)
├── run.sh                          # Mac/Linux startup
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── templates/
│   └── index.html                 # Web interface
├── static/
│   ├── css/
│   │   └── style.css              # Styling
│   └── js/
│       └── app.js                 # Frontend logic
└── downloader/
    ├── __init__.py
    ├── config.py
    ├── youtube_downloader.py
    └── tiktok_downloader.py
```

## 🛠️ Install FFmpeg

**Windows:**
```powershell
# Using Chocolatey (fastest)
choco install ffmpeg

# Or download from https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

## 🔧 Troubleshooting

### Issue: "Port 5000 already in use"
**Solution**: Change the port in `app.py`:
```python
app.run(debug=True, host="0.0.0.0", port=5001)  # Use 5001 instead
```

### Issue: "FFmpeg not found"
**Solution**: Install FFmpeg (see section above)

### Issue: Download fails
**Solution**:
- Check if the URL is correct
- Ensure you have internet connection
- Try a different video
- Update yt-dlp: `pip install --upgrade yt-dlp`

### Issue: Browser doesn't open automatically
**Solution**: Manually open `http://localhost:5000` in your browser

## 📱 Responsive Design

The web app works perfectly on:
- 🖥️ Desktop computers
- 💻 Laptops
- 📱 Tablets
- 📲 Mobile phones

## ⚠️ Legal Notice

**Personal Use Only**: This tool is for downloading videos you have permission to download. 

Always respect:
- Copyright laws
- Creator rights
- Terms of service of YouTube and TikTok
- Local regulations

## 🎓 Technology Stack

- **Backend**: Flask + Python
- **Frontend**: HTML5, CSS3, JavaScript
- **Video Processing**: yt-dlp + FFmpeg
- **HTTP**: CORS-enabled REST API

## 🐛 Report Issues

If you encounter bugs:
1. Check the console output
2. Try the latest version
3. Report on GitHub with details

## 📝 License

This project is provided as-is for educational purposes.

---

**Made with ❤️ for video enthusiasts**

### API Documentation

The app provides a REST API for backend integration:

**Download Endpoint**
```
POST /api/download
Content-Type: application/json

{
  "url": "video_url",
  "platform": "auto|youtube|tiktok",
  "quality": "best|high|medium|low",
  "audio_only": false,
  "audio_format": "mp3|m4a|wav|aac",
  "remove_watermark": true
}

Response:
{
  "status": "started",
  "session_id": "uuid",
  "message": "Message"
}
```

**Progress Endpoint**
```
GET /api/progress/{session_id}

Response:
{
  "status": "downloading|completed|error",
  "progress": 0-100,
  "message": "Status message"
}
```
