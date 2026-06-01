// ===========================
// Video Downloader App
// ===========================

class VideoDownloaderApp {
    constructor() {
        this.apiUrl = '/api';
        this.sessionId = null;
        this.isDownloading = false;
        this.selectedPlatform = 'auto';
        this.pollInterval = null;
        
        this.initElements();
        this.attachEventListeners();
    }

    initElements() {
        // Form elements
        this.videoUrl = document.getElementById('videoUrl');
        this.downloadBtn = document.getElementById('downloadBtn');
        this.quality = document.getElementById('quality');
        this.audioFormat = document.getElementById('audioFormat');
        this.audioOnly = document.getElementById('audioOnly');
        this.removeWatermark = document.getElementById('removeWatermark');
        
        // Platform buttons
        this.platformBtns = document.querySelectorAll('.platform-btn');
        
        // Sections
        this.formSection = document.getElementById('formSection');
        this.progressSection = document.getElementById('progressSection');
        
        // Progress elements
        this.progressFill = document.getElementById('progressFill');
        this.progressText = document.getElementById('progressText');
        this.progressMessage = document.getElementById('progressMessage');
        this.progressTitle = document.getElementById('progressTitle');
        this.statusIcon = document.getElementById('statusIcon');
        
        // Action buttons
        this.newDownloadBtn = document.getElementById('newDownloadBtn');
        
        // Toast
        this.toast = document.getElementById('toast');
    }

    attachEventListeners() {
        // Download button
        this.downloadBtn.addEventListener('click', () => this.handleDownload());
        
        // New download button
        this.newDownloadBtn.addEventListener('click', () => this.resetForm());
        
        // Platform selection
        this.platformBtns.forEach(btn => {
            btn.addEventListener('click', (e) => this.selectPlatform(e.target.closest('.platform-btn')));
        });
        
        // Enter key to download
        this.videoUrl.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.handleDownload();
        });
    }

    selectPlatform(btn) {
        this.platformBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        this.selectedPlatform = btn.dataset.platform;
    }

    async handleDownload() {
        const url = this.videoUrl.value.trim();
        
        if (!url) {
            this.showToast('❌ Vui lòng nhập URL video', 'error');
            return;
        }
        
        if (this.isDownloading) {
            this.showToast('⚠️ Đang tải xuống, vui lòng chờ', 'warning');
            return;
        }
        
        // Validate URL
        if (!this.isValidUrl(url)) {
            this.showToast('❌ URL không hợp lệ. Vui lòng kiểm tra lại', 'error');
            return;
        }
        
        await this.startDownload(url);
    }

    isValidUrl(url) {
        try {
            new URL(url);
            return url.includes('youtube.com') || url.includes('youtu.be') || 
                   url.includes('tiktok.com') || url.includes('vm.tiktok.com');
        } catch (e) {
            return false;
        }
    }

    async startDownload(url) {
        this.isDownloading = true;
        this.downloadBtn.disabled = true;
        
        try {
            // Show progress section
            this.showProgressSection();
            this.updateProgress('Đang chuẩn bị...', 0);
            
            // Send download request
            const response = await fetch(`${this.apiUrl}/download`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    url: url,
                    platform: this.selectedPlatform,
                    quality: this.quality.value,
                    audio_only: this.audioOnly.checked,
                    audio_format: this.audioFormat.value,
                    remove_watermark: this.removeWatermark.checked
                })
            });
            
            const data = await response.json();
            
            if (data.status === 'started') {
                this.sessionId = data.session_id;
                this.showToast(`🎬 ${data.message}`, 'success');
                this.pollProgress();
            } else if (data.status === 'error') {
                this.showError(data.message);
                this.resetForm();
            }
            
        } catch (error) {
            this.showError(`❌ Lỗi kết nối: ${error.message}`);
            this.resetForm();
        }
    }

    pollProgress() {
        if (this.pollInterval) clearInterval(this.pollInterval);
        
        this.pollInterval = setInterval(async () => {
            try {
                const response = await fetch(`${this.apiUrl}/progress/${this.sessionId}`);
                const data = await response.json();
                
                if (data.status === 'downloading') {
                    this.updateProgress(data.message, data.progress || 50);
                } else if (data.status === 'completed') {
                    clearInterval(this.pollInterval);
                    this.showSuccess(data.message);
                    this.isDownloading = false;
                } else if (data.status === 'error') {
                    clearInterval(this.pollInterval);
                    this.showError(data.message);
                    this.isDownloading = false;
                }
            } catch (error) {
                console.error('Error polling progress:', error);
            }
        }, 1000);
    }

    updateProgress(message, progress) {
        this.progressMessage.textContent = message;
        this.progressFill.style.width = progress + '%';
        this.progressText.textContent = Math.round(progress) + '%';
    }

    showProgressSection() {
        this.formSection.style.display = 'none';
        this.progressSection.style.display = 'block';
    }

    showSuccess(message) {
        this.progressTitle.textContent = '✅ Tải xuống thành công!';
        this.progressMessage.textContent = message;
        this.progressFill.style.width = '100%';
        this.progressText.textContent = '100%';
        
        this.statusIcon.classList.add('success');
        this.statusIcon.innerHTML = '<i class="fas fa-check-circle"></i>';
        
        this.showToast(message, 'success');
    }

    showError(message) {
        this.progressTitle.textContent = '❌ Lỗi';
        this.progressMessage.textContent = message;
        
        this.statusIcon.classList.add('error');
        this.statusIcon.innerHTML = '<i class="fas fa-times-circle"></i>';
        
        this.showToast(message, 'error');
    }

    resetForm() {
        // Clear form
        this.videoUrl.value = '';
        this.audioOnly.checked = false;
        this.removeWatermark.checked = true;
        this.quality.value = 'best';
        this.audioFormat.value = 'mp3';
        
        // Reset platform
        this.platformBtns.forEach(btn => btn.classList.remove('active'));
        this.platformBtns[0].classList.add('active');
        this.selectedPlatform = 'auto';
        
        // Reset progress
        this.progressFill.style.width = '0%';
        this.progressText.textContent = '0%';
        this.statusIcon.classList.remove('success', 'error');
        this.statusIcon.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        
        // Show form section
        this.formSection.style.display = 'flex';
        this.progressSection.style.display = 'none';
        
        // Reset state
        this.isDownloading = false;
        this.downloadBtn.disabled = false;
        this.sessionId = null;
        
        if (this.pollInterval) clearInterval(this.pollInterval);
        
        // Focus input
        this.videoUrl.focus();
    }

    showToast(message, type = 'info') {
        this.toast.textContent = message;
        this.toast.className = `toast show ${type}`;
        
        setTimeout(() => {
            this.toast.classList.remove('show');
        }, 4000);
    }
}

// ===========================
// Initialize App
// ===========================

document.addEventListener('DOMContentLoaded', () => {
    const app = new VideoDownloaderApp();
    
    // Auto-focus URL input
    app.videoUrl.focus();
    
    // Add paste functionality
    document.addEventListener('paste', (e) => {
        if (document.activeElement === app.videoUrl) {
            e.preventDefault();
            navigator.clipboard.readText().then(text => {
                app.videoUrl.value = text.trim();
            });
        }
    });
});
