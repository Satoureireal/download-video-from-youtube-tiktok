# 🚀 GitHub & Deploy Setup

## 📝 Bước 1: Push Code Lên GitHub

### 1.1 Tạo GitHub Repository

1. Đăng nhập: https://github.com
2. Click "+" → "New repository"
3. **Tên repo**: `download-video-tool`
4. **Description**: `Web tool to download videos from YouTube & TikTok`
5. **Public** (để ai cũng thấy)
6. Click "Create repository"

### 1.2 Push Code

Mở **PowerShell/Terminal** trong thư mục dự án và chạy:

```powershell
# Khởi tạo Git
git init

# Thêm tất cả files
git add .

# Commit lần đầu
git commit -m "Initial commit: Video Downloader Web App"

# Đặt tên branch chính là main
git branch -M main

# Thêm GitHub repo (THAY YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/download-video-tool.git

# Push lên GitHub
git push -u origin main
```

**Xong!** Code của bạn giờ ở GitHub 🎉

---

## 🌐 Bước 2: Deploy Lên Railway

Railway là cách **dễ nhất** để deploy app live trên internet.

### 2.1 Tạo Tài Khoản

1. Vào: https://railway.app
2. Click "Login with GitHub"
3. Cho phép Railway truy cập GitHub

### 2.2 Deploy

1. Click "New Project"
2. Chọn "Deploy from GitHub repo"
3. Tìm repo `download-video-tool`
4. Click "Deploy"
5. **Chờ 2-3 phút...**
6. ✅ Xong! Nhận URL like: `https://download-video-xxxx.railway.app`

### 2.3 Kiểm Tra Deployment

- Nhập URL vừa nhận được → Nếu thấy giao diện → **Thành công!** 🎉

---

## 🔄 Cập Nhật App

Sau khi deploy trên Railway, mỗi lần bạn push code:

```powershell
# Sửa code
# ...

# Commit & push
git add .
git commit -m "Fix: Something"
git push
```

Railway sẽ **tự động redeploy** trong vòng 1-2 phút! ⚡

---

## 📱 Share Với Bạn Bè

Sau khi có URL, bạn có thể:

- **Share link**: `https://download-video-xxxx.railway.app`
- Bạn bè mở link → Dùng ngay
- Không cần cài gì trên máy họ
- Chạy trên browser

---

## 💾 Các File Quan Trọng

Dưới đây là các file quan trọng để deploy hoạt động:

```
✅ app.py              # Flask backend
✅ requirements.txt    # Python dependencies + gunicorn
✅ Procfile           # Cách chạy app (gunicorn app:app)
✅ runtime.txt        # Python version (3.11.0)
✅ packages.txt       # System packages (ffmpeg)
✅ templates/         # HTML frontend
✅ static/            # CSS & JS
✅ downloader/        # Download modules
```

---

## 🆘 Troubleshooting

### ❌ "FFmpeg not found"

File `packages.txt` có chứa `ffmpeg` chưa?

Nếu chưa, tạo file `packages.txt`:
```
ffmpeg
```

Push lên GitHub → Railway sẽ cài tự động.

### ❌ "ModuleNotFoundError"

Kiểm tra `requirements.txt` có chứa tất cả library?

Nên có:
- Flask
- Flask-CORS  
- yt-dlp
- requests
- gunicorn

### ❌ Deployment failed

Check **Deploy Logs** trên Railway dashboard.

---

## 🎯 Tóm Tắt

1. ✅ Push GitHub: `git push`
2. ✅ Railway deploy: Kết nối GitHub
3. ✅ Nhận URL: `https://xxxxx.railway.app`
4. ✅ Share & dùng: Bạn bè dùng ngay

---

**Sẵn sàng? Bắt đầu push GitHub ngay!** 🚀
