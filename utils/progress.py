def make_progress_callback():
    def on_progress(stream, chunk, bytes_remaining):
        total = stream.filesize
        downloaded = total - bytes_remaining
        
        downloaded_mb = downloaded / (1024 * 1024)
        total_mb = total / (1024 * 1024)
        
        percent = (downloaded / total) * 100
        bar_length = 30
        filled = int(bar_length * downloaded / total)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        print(f"\r[{bar}] {percent:.1f}% | {downloaded_mb:.1f} MB / {total_mb:.1f} MB", end="", flush=True)
        
        if bytes_remaining == 0:
            print()
    
    return on_progress