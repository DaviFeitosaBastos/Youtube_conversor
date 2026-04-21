from ui.display import clear, cli, sleep
from ui.validation import yes_or_not
from pytubefix import YouTube
from pytubefix.cli import on_progress
from utils.log_utils import get_base_dir, get_logger
import subprocess
import shutil

log = get_logger(__name__)

FOLDER = get_base_dir() / "videos"
FOLDER.mkdir(exist_ok=True)

def get_video_info(url: str) -> None:
    """  
    Show to user all datas from an especified video like: views, likes, tittle, description etc...

    Get all the data from URL that was catched by Pytubefix
    """

    clear()

    # Get data from the video url
    yt = YouTube(url)

    def show_basic_info():
        """  
        Display: tittle | duration | views | author | channel ID | likes
        """
        cli.print(f"\n[bold]Title:[/bold] {yt.title}")
        cli.print(
            f"\n[bold]Duration:[/bold] " f"{f'{yt.length // 3600}:{(yt.length % 3600)//60:02d}:{yt.length % 60:02d}' if yt.length >= 3600 else f'{(yt.length % 3600)//60}:{yt.length % 60:02d}'}"
        ) # Format the duration in seconds to [HH:MM:SS]
        cli.print(f"\n[bold]Views:[/bold] {yt.views}")
        cli.print(f"\n[bold]Author:[/bold] {yt.author}")
        cli.print(f"\n[bold]Channel id:[/bold] {yt.channel_id}")
        cli.print(f"\n[bold]Likes:[/bold] {yt.likes}\n")

    # Loop for a better navegation :)
    while True:
        choice = input("Would you also like to see with the description? [y/n]: ").lower()

        if choice == 'y':
            show_basic_info()
            cli.print(f"[bold]Description:[/bold] {yt.description}\n")
            break

        elif choice == 'n':
            clear()
            print("\nOkay! just the basic info\n")
            show_basic_info()
            break

        else:
            cli.print('[red]Just <y> or <n> are allowed')
            sleep(1)
            clear()

    if not yes_or_not("Type Y to return or N to quit "):
        exit()


    
def download_high_res(url: str):
    """
    Downloads the highest resolution video with audio using ffmpeg to merge.
    """
    FFMPEG = shutil.which("ffmpeg")
    if not FFMPEG:
        cli.print("[red]ffmpeg not found! Please install it and add to PATH.[/red]")
        return

    yt = YouTube(url, on_progress_callback=on_progress)

    # Pega a melhor stream de vídeo (sem áudio) — até 4K
    video_stream = yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True).order_by("resolution").last()
    # Pega a melhor stream de áudio
    audio_stream = yt.streams.filter(adaptive=True, only_audio=True).order_by("abr").last()

    if video_stream is None or audio_stream is None:
        cli.print("[red]No stream found for this video.[/red]")
        return

    # Paths temporários e final
    temp_video = FOLDER / f"temp_video_{yt.video_id}.mp4"
    temp_audio = FOLDER / f"temp_audio_{yt.video_id}.mp4"
    final_path = FOLDER / f"{yt.title}.mp4"

    if final_path.exists():
        clear()
        cli.print(f"[yellow]Video already exists: {final_path.name}[/yellow]")
        if not yes_or_not("\nType Y to return or N to quit "):
            exit()
        return

    clear()
    cli.print(f"[green]Downloading video ({video_stream.resolution}): {yt.title}[/green]")
    try:
        video_stream.download(output_path=str(FOLDER), filename=temp_video.name)
    except Exception as e:
        log.error(f"Video download failed: {e}")
        return

    cli.print("[green]Downloading audio...[/green]")
    try:
        audio_stream.download(output_path=str(FOLDER), filename=temp_audio.name)
    except Exception as e:
        log.error(f"Audio download failed: {e}")
        return

    cli.print("[yellow]Merging video and audio...[/yellow]")
    try:
        subprocess.run([
            FFMPEG,
            "-i", str(temp_video),
            "-i", str(temp_audio),
            "-c:v", "copy",
            "-c:a", "aac",
            str(final_path)
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        log.error(f"Merge failed: {e}")
        return
    finally:
        # Sempre apaga os temporários, mesmo se falhar
        temp_video.unlink(missing_ok=True)
        temp_audio.unlink(missing_ok=True)

    cli.print(f"\n[green]Saved to: {FOLDER}[/green]")
    sleep(0.6)


def download_low_res(url: str):
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.get_lowest_resolution()

    if stream is None:
        cli.print("[red]No stream found for this video.[/red]")
        return

    video_path = FOLDER / stream.default_filename

    if video_path.exists():
        clear()
        cli.print(f"[yellow]Video already exists: {video_path.name}[/yellow]")
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

    cli.print(f"\n[green]Saved to: {FOLDER}[/green]")
    sleep(0.7)
