import subprocess
import shutil
from pytubefix import YouTube
from pytubefix.cli import on_progress
from ui.display import cli, sleep, clear
from ui.validation import yes_or_not
from utils.log_utils import get_base_dir, get_logger


log = get_logger(__name__)

BASE_DIR = get_base_dir()
FOLDER = BASE_DIR / "audios"
FOLDER.mkdir(exist_ok=True)

def download_track_youtube(url: str):
    """Downloads a track from YouTube and converts it to mp3."""

    FFMPEG = shutil.which("ffmpeg")
    if not FFMPEG:
        cli.print("[red]ffmpeg not found! Please install it and add to PATH.[/red]")
        return

    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.get_audio_only()

    # Verifica se encontrou stream
    if stream is None:
        cli.print("[red]No audio stream found for this video.[/red]")
        return

    temp_path = FOLDER / stream.default_filename
    final_path = temp_path.with_suffix(".mp3")

    if final_path.exists():
        clear()
        cli.print(f"[yellow]Track already exists: {final_path.name}[/yellow]")
        if not yes_or_not("\nType Y to return or N to quit "):
            exit()
        return

    clear()
    cli.print(f"[green]Downloading: {yt.title}[/green]")
    try:
        stream.download(output_path=str(FOLDER))  # str() aqui
    except Exception as e:
        log.error(f"Download failed: {e}")
        return

    cli.print("\n[yellow]Converting to mp3...[/yellow]")

    try:
        subprocess.run([
            FFMPEG, "-i", str(temp_path),
            "-q:a", "0", "-map", "a",
            str(final_path)
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        temp_path.unlink()
    except subprocess.CalledProcessError as e:
        log.error(f"Conversion failed {e}")
        return

    cli.print(f"[green]Saved to: {FOLDER}[/green]")
    sleep(0.7)
    