from rich.console import Console
import time 
from random import randint, uniform, shuffle, sample

cli = Console()

def clear():
    cli.clear()

def sleep(sec: int) -> None :
    time.sleep(sec)
    return None

def loading():
    total = randint(20, 50)
    bar_width = 40

    messages = {
        5:  "Loading libs...",
        8:  "Unpacking conversor...",
        10: "Initializing...",
        26: "Almost there...",
    }

    # mix the messages in random steps
    msg_steps = sorted(sample(range(3, total), min(4, total - 3)))
    msg_list = list(messages.values())
    shuffle(msg_list)
    dynamic_messages = dict(zip(msg_steps, msg_list))

    for i in range(total + 1):
        percent = int((i / total) * 100)
        filled = int((i / total) * bar_width)
        bar = "#" * filled + "." * (bar_width - filled)

        msg = dynamic_messages.get(i, "")
        clear()
        line = f"Loading... {percent:3}% [{bar}] {msg}"
        print(f"\r{line:<80}", end="", flush=True)

        if i in dynamic_messages:
            sleep(uniform(0.01, 0.03))  # random pauses
        else:
            sleep(uniform(0.2, 0.04))  # random speed to the loading messages

    print("\nDone!")


def print_exit():
    msg = "Exiting!!!!!"
    for i in range(len(msg) + 1):
        clear()
        cli.print(f"[bold red on white]{msg[:i]}[/bold red on white]", end="\r")
        sleep(0.1)
    sleep(0.3)
    clear()


def headers(header: str) -> None:
    if header == "Video Download":
        cli.print("[red]=[/red]" * 32)
        cli.print(f"[red]{header.center(32)}[/red]" )
        cli.print("[red]=[/red]" * 32)

    elif header == "Track Download":
        cli.print("[yellow]=[/yellow]" * 32)
        cli.print(f"[yellow]{header.center(32)}[/yellow]" )
        cli.print("[yellow]=[/yellow]" * 32)

    elif header == "GIF Converter":
        cli.print("[cyan]=[/cyan]" * 32)
        cli.print(f"[cyan]{header.center(32)}[/cyan]")
        cli.print("[cyan]=[/cyan]" * 32)
            
    elif header == "Main menu":
        cli.print("[green]=[/green]" * 32)
        cli.print(f"[green]{header.center(32)}[/green]" )
        cli.print("[green]=[/green]" * 32)
    else: 
        return None

def main_menu():
    cli.print("[green]1 - Download videos from[/green] [red][YOUTUBE][/red]")
    cli.print("[green]2 - Get the audio tack from[/green] [red][YOUTUBE][/red]")
    cli.print("[green]3 - Convert MP4 to GIF[/green]")
    cli.print("[green]0 -[/green] [red]Exit[/red]")



if __name__ == "__main__":
    ...
    
    
        