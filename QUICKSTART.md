# 🎬 Quick Start - Video Downloader Web

## ⚡ Fastest Setup (30 seconds)

### Windows
```
1. Find and double-click: run.bat
2. Browser opens automatically
3. Paste video URL and download!
```

### macOS/Linux
```bash
bash run.sh
# Browser opens automatically
```

## 🌐 What You'll See

A beautiful web interface with:
- 📝 URL input field
- 🎯 Platform selector (YouTube/TikTok/Auto)
- ⭐ Quality selector
- 🎵 Audio format options
- ✅ Real-time progress tracking

## 🎯 Common Tasks

### Download YouTube Video
1. Paste URL: `https://www.youtube.com/watch?v=...`
2. Select quality: "Tốt nhất"
3. Click "Tải video"
4. ✅ Done! Video saved to `./downloads/`

### Download as MP3
1. Paste URL
2. ✅ Check "Chỉ tải âm thanh"
3. Select format: MP3, M4A, or WAV
4. Click "Tải video"

### Download TikTok Without Watermark
1. Paste TikTok URL
2. ✅ Verify "Xóa logo/watermark" is checked
3. Click "Tải video"
4. ✅ No TikTok logo!

## 📁 Where Are Downloads?

All videos go to: `./downloads/` folder

## 🔗 Access the Web App

- **Automatic**: Browser opens at `http://localhost:5000`
- **Manual**: Open `http://localhost:5000` in any browser
- **From another device**: Use your computer's IP address (e.g., `http://192.168.1.x:5000`)

## ⚙️ Port Already In Use?

If port 5000 is busy, edit `app.py`:
```python
# Change this line:
app.run(debug=True, host="0.0.0.0", port=5000)

# To this:
app.run(debug=True, host="0.0.0.0", port=5001)

# Then access at http://localhost:5001
```

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python not found" | Install Python from python.org |
| "FFmpeg not found" | Run: `choco install ffmpeg` (Windows) or `brew install ffmpeg` (Mac) |
| "Module not found" | Run: `pip install -r requirements.txt` |
| Browser won't open | Manually go to `http://localhost:5000` |
| Download fails | Check URL format, try different video |

## 🎨 Features

✨ Modern dark theme with animated background
📱 Responsive design (works on phone, tablet, desktop)
⚡ Fast, lightweight interface
🎯 Simple and intuitive to use
💬 Clear Vietnamese interface

## 📚 For More Info

- Read `README.md` for detailed documentation
- Check console output for error messages
- Try a different video if one fails

## 🚀 Pro Tips

1. **Batch downloads**: Download multiple videos one after another
2. **Best quality**: Select "Tốt nhất" for highest resolution
3. **Save space**: Use "Chỉ tải âm thanh" for audio-only files
4. **Network issues**: If stuck, refresh browser and retry

---

**That's it!** 🎉 You're ready to download videos.

**Questions?** Check README.md for more details.

