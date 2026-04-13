from rich.prompt import Prompt
from rich.panel import Panel
from ui.display import sleep, clear, cli
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, RegexMatchError
from urllib.parse import urlparse
from pathlib import Path
from utils.log_utils import get_logger

log = get_logger(__name__)

def url_validate(url: str) -> bool:
    """
    Validates if the given string is a valid and accessible YouTube URL.
    """
    # 1. Check if the url has an basic url structure
    parsed = urlparse(url)
    if not (parsed.scheme in ("http", "https") and parsed.netloc):
        cli.print("[red]Invalid URL format[/red]")
        sleep(0.6)
        clear()
        return False

    # 2. Check if it's youtube url
    if not ("youtube.com" in parsed.netloc or "youtu.be" in parsed.netloc):
        cli.print("[red]This is not a YouTube URL[/red]")
        sleep(0.6)
        clear()
        return False

    # 3. Check if the video exist or is available
    try:
        yt = YouTube(url)
        _ = yt.title
        return True
    except VideoUnavailable:
        log.error(f"Unvailable video: This video can not exist")
        return False
    except RegexMatchError:
        log.error(f"Invalid Url: expected a valid URL")
        return False
    except Exception as e:
        log.error(f"Invalid Url: {e}")
        sleep(0.6)
        clear()
        return False

def yes_or_not(message: str) -> bool:
    """
    Prompts the user for a Y/N confirmation. Returns True if 'Y', False if 'N'.
    """
    while True:
        cli.print(Panel(f"[bold yellow]{message}[/bold yellow]", 
                        border_style="yellow", 
                        expand=False))
        
        choice = Prompt.ask("\n[bold green]Choice[/bold green]", 
                            choices=["Y", "N", "y", "n"], 
                            show_choices=True).strip().upper()
        
        if choice in ("Y", "N"):
            if choice == "Y":
                cli.print("[bold green]✔ Confirmed![/bold green]")
            else:
                cli.print("[bold red]✘ Cancelled![/bold red]")
            sleep(0.5)
            clear()
            return choice == "Y"
        
        cli.print("[bold red]✘ Invalid input! Please enter Y or N.[/bold red]")
        sleep(0.8)
        clear()


def get_int_input() -> int | None:
    """ 
    Reads an integer from user input. Returns None on invalid input.
    """
    while True:
        try:
            choice = int(Prompt.ask(f"\n[green]Choice[/green]"))
            clear()
            if not choice == 0:
                cli.print(f"\n[green]Option selected {choice}")
                sleep(1)
            return choice
        except ValueError as e:
            log.warning(f"Invalid input: expected a number {e}")
            sleep(0.5)
            return None



def validate_path(path: str) -> bool:
    p = Path(path)
    if p.exists():
        return True
    else:
        cli.print("[red]This path doesn't exist[/red]")
        sleep(0.6)

def pick_file(folder: Path, extension: str) -> Path | None:
    """
    Lists files with the given extension in the folder and lets the user pick one.
    """
    files = list(folder.glob(f"*{extension}"))

    if not files:
        cli.print(f"[red]No {extension} files found in {folder}[/red]")
        sleep(0.6)
        return None

    cli.print(f"\n[bold]Available {extension} files:[/bold]")
    for i, file in enumerate(files, start=1):
        cli.print(f"[cyan]{i} - {file.name}[/cyan]")

    while True:
        try:
            choice = int(input("\nChoice: "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            cli.print("[red]Invalid option![/red]")
            sleep(0.5)
        except ValueError:
            log.warning(f"Invalid input: expected number")
            sleep(0.5)
            
            

if __name__ == "__main__":
    yes_or_not("Wanna go back [Y/N]")
    pass