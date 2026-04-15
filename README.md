# Youtube Conversor

A Python CLI tool for downloading YouTube videos, audio tracks, and converting MP4 files to GIF directly from the terminal, with a clean menu-driven interface powered by Rich.

---

## Features

- Download YouTube videos in **high or low resolution**
- Download **audio tracks** from YouTube as MP3
- Convert **MP4 videos to GIF** with customizable settings (FPS, resolution, trim)
- View **video metadata** before downloading
- Interactive menu with URL validation
- Clean terminal UI using Rich

---

## Project Structure

```
Youtube_conversor/
├── main.py               # Application entry point
├── router.py             # Menu routing and navigation logic
├── .gitignore            # Ignore uploads of files unnecessary
├── README.md             # You're reading this right now
├── README.pt-br.md       # README in pt-BR
├── requirements.txt      # All denpendency 
├── __init__.py
├── gifs/
│   └── # Here will be the gifs converted
├── web/
│   ├── __init__.py
│   └── log_utils.py     # Shared utilities (get_base_dir)(logger)
├── service/
│   ├── video_service.py  # Video download logic (high res, low res, info)
│   ├── track_service.py  # Audio track download logic
│   └── gif_service.py    # MP4 to GIF conversion logic
└── ui/
    ├── __init__.py
    ├── display.py        # CLI display helpers (headers, menus, loading)
    └── validation.py     # Input validation (URL, integers, yes/no, file picker)
```

---

## Development Setup

**Create and activate a virtual environment:**

```bash
python -m venv venv

# Linux
source venv/bin/activate

# Windows
venv\Scripts\Activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

> Make sure `ffmpeg` is installed on your system and available in PATH.
>
> Linux: `sudo apt install ffmpeg`
>
> Windows: https://ffmpeg.org/download.html

---

## Usage

```bash
# linux
python3 main.py

# windows
python main.py
```

Navigate using the numbered options:

```
================================
         Main menu
================================
1 - Download videos from [YOUTUBE]
2 - Get the audio track from [YOUTUBE]
3 - Convert MP4 to GIF
0 - Exit
```

After selecting an option, follow the prompts in the terminal.

---

## Output Folders

All files are saved automatically on first run:

| Folder | Content |
|---|---|
| `videos/` | Downloaded MP4 videos |
| `audios/` | Downloaded MP3 tracks |
| `gifs/` | Converted GIF files |

---

## Building the Executable

```bash
pyinstaller --onefile --paths . main.py
```

> The executable will be generated in the `dist/` folder.
> The `videos/`, `audios/`, and `gifs/` folders are created automatically on first run alongside the executable.

To rebuild, clean the previous build first:

```bash
rm -rf build/ dist/ main.spec
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `pytubefix` | YouTube video/audio downloading |
| `yt-dlp` | Alternative download backend |
| `ffmpeg-python` | MP4 to GIF conversion |
| `rich` | Terminal UI styling |

---
## Roadmap
- [ ] Run on web application
- [ ] Make a GUI properly instead of terminal
- [ ] Support for multiples providers beyond Youtube

---

## Notes

- This tool is intended for personal use only.
- Respect YouTube's Terms of Service when downloading content.

---

## Author

[DaviFeitosaBastos](https://github.com/DaviFeitosaBastos)
