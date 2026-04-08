from ui.display import cli, clear, sleep, headers
from ui.validation import yes_or_not, get_int_input, url_validate
from service.video_service import download_high_res, download_low_res, get_video_info
from service.track_service import download_track_youtube



HEADER1 = "Video Download"
HEADER2 = "Track Download"

def videos_downloader_menu():
    """
    Display the video download menu and handle user input.

    Options:
        1 - Get higher resolution videos
        2 - Get lower resolution videos
        3 - Get the videos info
        0 - Back to main menu
    """
    sub_routes = {
        1: download_high_res,
        2: download_low_res,
        3: get_video_info,
    }

    while True:
        clear()
        headers(HEADER1)
        cli.print("[red]1 - Get higher resolution videos[/red]")
        cli.print("[red]2 - Get lower resolution videos[/red]")
        cli.print("[red]3 - Get the videos info[/red]")
        cli.print("[red]0 - Back to main menu[/red]")

        choice = get_int_input()

        if choice == None:
            continue
        elif not choice in [1,2,3,0]:
            cli.print("[red]Invalid option![/red]")
            sleep(0.5)
            continue
        if choice == 0:
            clear()
            if yes_or_not("Wanna go back [Y/N]: "):
                break
            continue  # ← se o user responde "N", volta ao menu

        handler = sub_routes.get(choice)
        if handler:
            url = input("\nURL: ")
            if not url_validate(url):
                continue
            handler(url)



def tracks_downloader_menu():
    """
    Display the track download menu and handle user input.

    Options:
        1 - Get the track from [YOUTUBE]
        0 - Back to main menu
    """
    sub_routes = {
        1: download_track_youtube,
    }

    while True:
        clear()
        headers(HEADER2)
        cli.print("[yellow]1 - Get the track from[/yellow] [red][YOUTUBE][/red]")
        cli.print("[yellow]0 - Back to main menu[/yellow]")

        choice = get_int_input()

        if choice == None:
            continue
        elif not choice in [1,0]:
            cli.print("[red]Invalid option![/red]")
            sleep(0.5)
            continue

        if choice == 0:
            clear()
            if yes_or_not("Wanna go back [Y/N]: "):
                break
            continue

        handler = sub_routes.get(choice)
        if handler:
            url = input("\nURL: ")
            if url_validate(url):
                handler(url)

# Route map: menu option -> handler function
routes = {
    1: videos_downloader_menu,  # Video downloader
    2: tracks_downloader_menu  # Track downloader
}

if __name__ == "__main__":
    videos_downloader_menu()