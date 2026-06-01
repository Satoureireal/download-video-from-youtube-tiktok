# 🚀 Deploy Guide - Video Downloader

Hướng dẫn deploy lên các nền tảng **miễn phí** từ GitHub.

## 📋 Các Tùy Chọn Deploy

### 1️⃣ **Railway.app** (Khuyến Khích - Dễ Nhất) ⭐

Railway là nền tảng miễn phí tốt nhất hiện nay:
- ✅ Miễn phí $5/tháng (đủ cho hầu hết)
- ✅ Deploy tự động từ GitHub
- ✅ Hỗ trợ Python + FFmpeg
- ✅ UI đẹp, dễ sử dụng

#### Cách Deploy:

1. **Tạo tài khoản**: https://railway.app
2. **Login bằng GitHub**
3. **Tạo Project**:
   - Click "Create Project"
   - Chọn "Deploy from GitHub repo"
   - Chọn repo `download-video-tool`
4. **Thêm biến môi trường** (nếu cần):
   - Không cần thiết, tự động detect `requirements.txt`
5. **Deploy tự động!** ✅

Sau khi deploy xong:
- Bạn sẽ có URL: `https://xxxx.railway.app`
- Share URL này cho ai cũng được
- Mỗi push lên GitHub tự động update

---

### 2️⃣ **Render.com**

Render cũng miễn phí nhưng hơi khác một chút:

1. **Tạo tài khoản**: https://render.com
2. **Click "New +"** → **"Web Service"**
3. **Chọn GitHub repo**
4. **Settings**:
   - Name: `video-downloader`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. **Deploy**
6. Nhận URL public ✅

---

### 3️⃣ **Replit.com**

Cách đơn giản nhất (không cần GitHub):

1. Tạo tài khoản: https://replit.com
2. Click "Import from GitHub"
3. Paste link repo: `https://github.com/your-username/download-video-tool`
4. Replit sẽ tự setup
5. Click "Run" → Nhận URL public ✅

---

## 📝 Các Bước Trước Khi Deploy

### 1. Push Code Lên GitHub

```bash
# 1. Tạo GitHub repo (empty, không có README)
# Đặt tên: download-video-tool

# 2. Mở terminal/PowerShell trong thư mục dự án
cd "c:\Users\Administrator\Desktop\download video from youtube tiktok"

# 3. Khởi tạo Git (nếu chưa)
git init
git add .
git commit -m "Initial commit - Video Downloader Web"

# 4. Thêm remote GitHub
git remote add origin https://github.com/YOUR-USERNAME/download-video-tool.git

# 5. Push lên GitHub
git branch -M main
git push -u origin main
```

### 2. Chỉnh Sửa Cần Thiết

**Thêm FFmpeg để hoạt động trên cloud:**

Tạo file `packages.txt` (để Railway/Render cài FFmpeg):

```
ffmpeg
```

---

## 🔗 URL Kết Quả

Sau khi deploy xong, bạn sẽ có:

```
https://video-downloader-xxxxxx.railway.app
```

Share URL này → Ai cũng có thể dùng! 🎉

---

## 📊 So Sánh Các Nền Tảng

| Nền Tảng | Miễn Phí | Setup | Tốc Độ | Khuyến Khích |
|----------|---------|-------|--------|------------|
| **Railway** | $5/tháng | ⭐⭐⭐ | ⚡⚡⚡ | ✅ Tốt nhất |
| **Render** | Có (giới hạn) | ⭐⭐ | ⚡⚡ | Tạm được |
| **Replit** | Có | ⭐⭐⭐ | ⚡ | Yếu nhất |
| **Heroku** | ❌ Hết (từ Nov 2022) | N/A | N/A | Không dùng |

---

## 🚨 Có Thể Gặp Vấn Đề

### ❌ "FFmpeg not found"
**Fix**: Tạo file `packages.txt` với nội dung:
```
ffmpeg
```

### ❌ "Port already in use"
**Fix**: Code đã hỗ trợ, sẽ tự detect port từ hosting

### ❌ "Deployment failed"
**Check**:
1. `requirements.txt` đầy đủ?
2. `Procfile` có đúng không?
3. `runtime.txt` chỉ Python 3.11+?

---

## ✅ Kiểm Tra Deployment

Sau khi deploy, test:

```
https://your-app-url.railway.app
```

Nếu thấy giao diện → Thành công! 🎉

---

## 🎯 Tóm Tắt Nhanh

1. **Push GitHub**: `git push`
2. **Vào Railway.app**: Kết nối GitHub
3. **Deploy**: Tự động từ GitHub push
4. **Share URL**: Cho bạn bè dùng
5. **Done!** ✨

---

## 💡 Tips

- Railway free $5/tháng = tải hơn 1000 video
- Mỗi push GitHub tự động update trên live
- Có thể share URL với bạn, họ dùng ngay
- FFmpeg có sẵn, không cần cài gì thêm

---

**Sẵn sàng deploy? Chọn Railway → Click Deploy!** 🚀
