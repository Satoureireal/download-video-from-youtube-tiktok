"""GUI application for video downloader"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
import threading
import sys
from downloader.youtube_downloader import YouTubeDownloader
from downloader.tiktok_downloader import TikTokDownloader


class VideoDownloaderGUI:
    """GUI for video downloader tool"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Video Downloader - YouTube & TikTok")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Style
        style = ttk.Style()
        style.theme_use("clam")
        
        self.output_dir = Path("./downloads")
        self.is_downloading = False
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create GUI widgets"""
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="📥 Video Downloader", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # URL input
        ttk.Label(main_frame, text="Video URL:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.url_var = tk.StringVar()
        url_entry = ttk.Entry(main_frame, textvariable=self.url_var, width=70)
        url_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Platform selection
        ttk.Label(main_frame, text="Platform:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.platform_var = tk.StringVar(value="auto")
        platform_frame = ttk.Frame(main_frame)
        platform_frame.grid(row=2, column=1, columnspan=2, sticky=tk.W, pady=5)
        ttk.Radiobutton(platform_frame, text="Auto-detect", variable=self.platform_var, value="auto").pack(side=tk.LEFT)
        ttk.Radiobutton(platform_frame, text="YouTube", variable=self.platform_var, value="youtube").pack(side=tk.LEFT)
        ttk.Radiobutton(platform_frame, text="TikTok", variable=self.platform_var, value="tiktok").pack(side=tk.LEFT)
        
        # Quality selection
        ttk.Label(main_frame, text="Quality:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.quality_var = tk.StringVar(value="best")
        quality_combo = ttk.Combobox(main_frame, textvariable=self.quality_var, 
                                     values=["best", "high", "medium", "low"], state="readonly", width=20)
        quality_combo.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Audio format
        ttk.Label(main_frame, text="Audio Format:").grid(row=3, column=2, sticky=tk.E, padx=10, pady=5)
        self.audio_format_var = tk.StringVar(value="mp3")
        audio_combo = ttk.Combobox(main_frame, textvariable=self.audio_format_var,
                                   values=["mp3", "m4a", "wav", "aac"], state="readonly", width=10)
        audio_combo.grid(row=3, column=3, sticky=tk.W, pady=5)
        
        # Options
        ttk.Label(main_frame, text="Options:").grid(row=4, column=0, sticky=tk.W, pady=5)
        options_frame = ttk.Frame(main_frame)
        options_frame.grid(row=4, column=1, columnspan=3, sticky=tk.W, pady=5)
        
        self.audio_only_var = tk.BooleanVar()
        ttk.Checkbutton(options_frame, text="Audio only", variable=self.audio_only_var).pack(side=tk.LEFT)
        
        self.remove_watermark_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Remove watermark (TikTok)", variable=self.remove_watermark_var).pack(side=tk.LEFT)
        
        # Output directory
        ttk.Label(main_frame, text="Output Folder:").grid(row=5, column=0, sticky=tk.W, pady=5)
        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=5, column=1, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        self.output_label = ttk.Label(output_frame, text=str(self.output_dir), foreground="blue")
        self.output_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Button(output_frame, text="Browse...", command=self._browse_output).pack(side=tk.LEFT, padx=5)
        
        # Custom filename
        ttk.Label(main_frame, text="Custom Filename:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.filename_var = tk.StringVar()
        filename_entry = ttk.Entry(main_frame, textvariable=self.filename_var, width=50)
        filename_entry.grid(row=6, column=1, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        ttk.Label(main_frame, text="(leave empty for auto)", foreground="gray").grid(row=6, column=4, sticky=tk.W, padx=5)
        
        # Download button
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=4, pady=15)
        
        self.download_btn = ttk.Button(button_frame, text="📥 Download", command=self._download)
        self.download_btn.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Clear", command=self._clear).pack(side=tk.LEFT, padx=5)
        
        # Output log
        ttk.Label(main_frame, text="Download Log:").grid(row=8, column=0, sticky=tk.W, pady=(10, 5))
        
        self.log_text = scrolledtext.ScrolledText(main_frame, height=15, width=80, state=tk.DISABLED)
        self.log_text.grid(row=9, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(9, weight=1)
    
    def _browse_output(self):
        """Browse for output directory"""
        folder = filedialog.askdirectory(initialdir=str(self.output_dir))
        if folder:
            self.output_dir = Path(folder)
            self.output_label.config(text=str(self.output_dir))
    
    def _log(self, message: str):
        """Add message to log"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update()
    
    def _clear(self):
        """Clear log and inputs"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.url_var.set("")
    
    def _download(self):
        """Start download"""
        url = self.url_var.get().strip()
        
        if not url:
            messagebox.showerror("Error", "Please enter a video URL")
            return
        
        if self.is_downloading:
            messagebox.showwarning("Warning", "Download already in progress")
            return
        
        self.is_downloading = True
        self.download_btn.config(state=tk.DISABLED)
        
        # Start download in separate thread
        thread = threading.Thread(target=self._download_worker, args=(url,), daemon=True)
        thread.start()
    
    def _download_worker(self, url: str):
        """Download worker thread"""
        try:
            platform = self.platform_var.get()
            
            # Auto-detect platform
            if platform == "auto":
                if "youtube.com" in url or "youtu.be" in url:
                    platform = "youtube"
                elif "tiktok.com" in url:
                    platform = "tiktok"
                else:
                    self._log("❌ Error: Could not detect platform. Please specify manually.")
                    return
            
            self._log(f"🎬 Downloading from {platform.upper()}...\n")
            
            quality = self.quality_var.get()
            audio_only = self.audio_only_var.get()
            audio_format = self.audio_format_var.get()
            filename = self.filename_var.get().strip() or None
            
            if platform == "youtube":
                downloader = YouTubeDownloader(str(self.output_dir))
                success = downloader.download(
                    url=url,
                    quality=quality,
                    audio_only=audio_only,
                    audio_format=audio_format,
                    filename=filename
                )
            else:  # tiktok
                downloader = TikTokDownloader(str(self.output_dir))
                success = downloader.download(
                    url=url,
                    quality=quality,
                    remove_watermark=self.remove_watermark_var.get(),
                    audio_only=audio_only,
                    audio_format=audio_format,
                    filename=filename
                )
            
            if success:
                self._log(f"✅ Download completed! File saved in: {self.output_dir}")
                messagebox.showinfo("Success", "Download completed successfully!")
            else:
                self._log("❌ Download failed. Check the log above.")
                messagebox.showerror("Error", "Download failed. Please check your URL and try again.")
        
        except Exception as e:
            self._log(f"❌ Error: {str(e)}")
            messagebox.showerror("Error", f"Error: {str(e)}")
        
        finally:
            self.is_downloading = False
            self.download_btn.config(state=tk.NORMAL)


def main():
    root = tk.Tk()
    app = VideoDownloaderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
