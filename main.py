# Display imports
from ui.display import cli, clear, sleep, headers,main_menu,loading, print_exit
# Validation imports
from ui.validation import get_int_input
# ROUTER import
from router import routes
import logging 


def main():
    """ 
    Main application loop. Handles navigation between menus. 
    """
    HEADER = "Main menu"

    loading()
    while True:      
        clear()
        headers(HEADER)
        main_menu()  

        choice = get_int_input()

        if choice == None:
            continue
        elif not choice in [1, 2, 3, 0]:
            cli.print("[red]Invalid option![/red]")
            sleep(0.5)
            continue
        if choice == 0:
            print_exit()
            break
        
        # Dispatch to the selected menu handler
        handler = routes.get(choice)
        if handler:
            handler()
        
    
if __name__ == "__main__":
    main()
    