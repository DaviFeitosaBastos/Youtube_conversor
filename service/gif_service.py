from ui.display import clear, cli, sleep
from ui.validation import yes_or_not, validate_path
from pathlib import Path
import ffmpeg
from utils import get_base_dir, get_logger

log = get_logger(__name__)


FOLDER = get_base_dir() / "gifs"
FOLDER.mkdir(exist_ok=True)


def _get_time_input(label: str) -> str:
    """
    Prompts the user for a time input in HH:MM:SS format.
    """
    while True:
        value = input(f"\n{label} (HH:MM:SS): ").strip()
        parts = value.split(":")
        if len(parts) == 3 and all(p.isdigit() for p in parts):
            return value
        cli.print("[red]Invalid format. Use HH:MM:SS (ex: 00:00:05)[/red]")
        sleep(0.5)


def _get_int_with_default(label: str, default: int) -> int:
    """
    Prompts the user for an integer input with a default fallback.
    """
    while True:
        value = input(f"\n{label} (default: {default}): ").strip()
        if value == "":
            return default
        if value.isdigit() and int(value) > 0:
            return int(value)
        cli.print("[red]Invalid value. Enter a positive number.[/red]")
        sleep(0.5)


def convert_mp4_to_gif(path: str) -> None:
    """
    Converts a MP4 file to GIF with user-defined settings.
    """
    clear()

    if not validate_path(path):
        return

    mp4_path = Path(path)

    if mp4_path.suffix.lower() != ".mp4":
        cli.print("[red]File must be a .mp4[/red]")
        sleep(0.6)
        return

    start_time = _get_time_input("Start time")
    end_time = _get_time_input("End time")
    fps = _get_int_with_default("FPS", 10)
    width = _get_int_with_default("Width (px)", 480)

    gif_name = mp4_path.stem + ".gif"
    gif_path = FOLDER / gif_name

    if gif_path.exists():
        clear()
        cli.print(f"[yellow]GIF already exists: {gif_path.name}[/yellow]")
        if not yes_or_not("\nType Y to return or N to quit "):
            exit()
        return

    clear()
    cli.print(f"[green]Converting: {mp4_path.name}[/green]")

    log.info("Starting conversion....") # Log system
    try:
        palette_path = get_base_dir() / "palette.png"

        # Step 1: generate palette for better GIF quality
        (
            ffmpeg
            .input(str(mp4_path), ss=start_time, to=end_time)
            .filter("fps", fps)
            .filter("scale", width, -1, flags="lanczos")
            .filter("palettegen")
            .output(str(palette_path))
            .overwrite_output()
            .run(quiet=True)
        )

        # Step 2: convert using the palette
        video_stream = ffmpeg.input(str(mp4_path), ss=start_time, to=end_time)
        palette_stream = ffmpeg.input(str(palette_path))

        (
            ffmpeg
            .filter(
                [
                    video_stream.filter("fps", fps).filter("scale", width, -1, flags="lanczos"),
                    palette_stream
                ],
                "paletteuse"
            )
            .output(str(gif_path))
            .overwrite_output()
            .run(quiet=True)
        )

        palette_path.unlink(missing_ok=True)

        cli.print(f"\n[green]Saved to: {gif_path}[/green]")

    except ffmpeg.Error as e:
        log.error(f"Conversion error: {e}")

    sleep(0.7)