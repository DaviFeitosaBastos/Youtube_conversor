from ui.display import clear, cli, sleep
from ui.validation import url_validate, yes_or_not
from pytubefix import YouTube
from pytubefix.cli import on_progress
from rich.console import Console
from pathlib import Path
import sys

def get_base_dir():
    if hasattr(sys, '_MEIPASS'):
        return Path(sys.executable).parent
    return Path(__file__).parent.parent

FOLDER = get_base_dir() / "videos"
FOLDER.mkdir(exist_ok=True)

def get_video_info(url: str) -> None:
    """
    Fetches and displays video info.
    """
    clear()
    yt = YouTube(url)
    cli.print(f"[bold]Title:[/bold] {yt.title}")
    cli.print(f"[bold]Duration:[/bold] {yt.length}s")
    cli.print(f"[bold]Views:[/bold] {yt.views}")
    cli.print(f"[bold]Author:[/bold] {yt.author}")
    cli.print(f"[bold]Rating:[/bold] {yt.rating}")
    cli.print(f"[bold]Channel id:[/bold] {yt.channel_id}")
    cli.print(f"[bold]Likes:[/bold] {yt.likes}\n")
    if not yes_or_not("Type Y to return or N to quit "):
        exit()
    
def download_high_res(url: str):
    """Downloads the highest resolution video."""
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    video_path = FOLDER / stream.default_filename

    if video_path.exists():
        clear()
        cli.print(f"[yellow]Video already exists: {video_path.name}[/yellow]")
        if not yes_or_not("\nType Y to return or N to quit "):
            exit()
        return
    
    clear()
    cli.print(f"[green]Downloading: {yt.title}[/green]")
    stream.download(output_path=FOLDER)
    cli.print(f"\n[green]Saved to: {FOLDER}[/green]")
    sleep(0.6)

def download_low_res(url: str):
    """
    Downloads the lowest resolution video.
    """
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.get_lowest_resolution()
    video_path = FOLDER / stream.default_filename

    if video_path.exists():
        clear()
        cli.print(f"[yellow]Video already exists: {video_path.name}[/yellow]")
        if not yes_or_not("\nType Y to return or N to quit "):
            exit()
        return
    
    clear()
    cli.print(f"[green]Downloading: {yt.title}[/green]")
    stream.download(output_path=FOLDER)
    cli.print(f"\n[green]Saved to: {FOLDER}[/green]")
    sleep(0.7)
