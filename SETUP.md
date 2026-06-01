# Getting Started with Video Downloader Web

## 🚀 Start Here!

Choose your operating system:

### Windows Users 👇

**Easiest way:**
1. Find `run.bat` in the project folder
2. **Double-click it** ✨
3. Wait for your browser to open
4. Start downloading videos!

**If that doesn't work:**
```powershell
# Open PowerShell or Command Prompt in the project folder
python app.py
# Then go to http://localhost:5000
```

### macOS & Linux Users 👇

**Easiest way:**
```bash
bash run.sh
# Browser will open automatically
```

**Alternative:**
```bash
python3 app.py
# Then go to http://localhost:5000
```

## ⚙️ First Time Setup

If you get any errors about missing modules:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Check FFmpeg is installed
ffmpeg -version
```

### Need to install FFmpeg?

**Windows:**
```powershell
choco install ffmpeg
# If that doesn't work, download from ffmpeg.org
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

## 🎬 Using the App

Once the app is running:

1. **Paste a video URL**
   - YouTube: https://www.youtube.com/watch?v=...
   - TikTok: https://www.tiktok.com/@.../video/...

2. **Choose your options:**
   - Platform: Auto-detect or select
   - Quality: Best, High, Medium, or Low
   - Format: MP3, M4A, WAV, AAC

3. **Click "Tải video"**

4. **Wait for download to complete** ✅

Downloads are saved to `./downloads/` folder

## 🆘 Common Issues

### "Python not found"
- Install from https://www.python.org
- Make sure "Add Python to PATH" is checked during installation

### "FFmpeg not found"
- Perform FFmpeg installation (see above)

### "Module not found" (like Flask)
- Run: `pip install -r requirements.txt`

### "Port 5000 in use"
- Edit `app.py` and change port 5000 to 5001
- Access at http://localhost:5001

### Download keeps failing
- Check if the URL is correct
- Try a different video
- Update yt-dlp: `pip install --upgrade yt-dlp`

## 📖 For More Help

- See **README.md** for complete documentation
- See **QUICKSTART.md** for quick reference
- Check browser console (F12) for error messages

## 🎯 What's Next?

1. ✅ Run `run.bat` (Windows) or `bash run.sh` (Mac/Linux)
2. ✅ Paste a video URL
3. ✅ Download your first video!
4. ✅ Enjoy! 🎉

---

**Ready to download?** Run the startup script now! 🚀
