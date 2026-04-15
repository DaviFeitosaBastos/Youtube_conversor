from ui.display import clear, cli, sleep
from ui.validation import yes_or_not
from pytubefix import YouTube
from pytubefix.cli import on_progress
from utils.log_utils import get_base_dir, get_logger

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
    Downloads the highest resolution video.
    """
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    video_path = get_base_dir() / stream.default_filename

    if video_path.exists():
        clear()
        cli.print(f"[yellow]Video already exists: {video_path.name}[/yellow]")
        if not yes_or_not("\nType Y to return or N to quit "):
            exit()
        return
    
    clear()
    cli.print(f"[green]Downloading: {yt.title}[/green]")
    try:
        stream.download(output_path=FOLDER)
    except Exception as e:
        log.error(f"Download failed: {e}")
        return
    
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

    try:
        stream.download(output_path=FOLDER)
    except Exception as e:
        log.error(f"Download failed: {e}")
        return
    
    cli.print(f"\n[green]Saved to: {FOLDER}[/green]")
    sleep(0.7)
