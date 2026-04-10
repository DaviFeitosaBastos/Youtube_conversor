# Youtube Conversor

A Python CLI tool for downloading YouTube videos and audio tracks directly from the terminal, with a clean menu-driven interface powered by Rich.

---

## Features

- Download YouTube videos in **high or low resolution**
- Download **audio tracks** from YouTube
- View **video metadata** before downloading
- Interactive menu with URL validation
- Clean terminal UI using Rich

---

## Project Structure

```
Youtube_conversor/
├── main.py               # Application entry point
├── router.py             # Menu routing and navigation logic
├── requirements.txt
├── __init__.py
├── service/
│   ├── video_service.py  # Video download logic (high res, low res, info)
│   └── track_service.py  # Audio track download logic
└── ui/
    ├── display.py        # CLI display helpers (headers, menus, loading)
    └── validation.py     # Input validation (URL, integers, yes/no)
```

---

## Requirements

- Python 3.10+
- ffmpeg installed and available in PATH

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

Navigate using the numbered options:

```
================================
         Main menu
================================
1 - Download videos from [YOUTUBE]
2 - Get the audio track from [YOUTUBE]
0 - Exit
```

After selecting an option, paste the YouTube URL when prompted.

---

## Dependencies

| Package | Purpose |
|---|---|
| `pytubefix` | YouTube video/audio downloading |
| `yt-dlp` | Alternative download backend |
| `ffmpeg-python` | Media processing |
| `rich` | Terminal UI styling |
| `PyMuPDF` | PDF handling |
| `pdf2docx` | Document conversion |
| `opencv-python-headless` | Image/video processing |

---

## Notes

- This tool is intended for personal use only.
- Respect YouTube's Terms of Service when downloading content.
- Make sure `ffmpeg` is installed on your system for media processing to work correctly.

---

## Author

[DaviFeitosaBastos](https://github.com/DaviFeitosaBastos)
