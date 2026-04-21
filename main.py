# Display imports
from ui.display import cli, clear, sleep, headers,main_menu,loading, print_exit
# Validation imports
from ui.validation import get_int_input, main_input_validated
# ROUTER import
from router import routes


def main():
    """ 
    Main application loop. Handles navigation between menus. 
    """
    HEADER = "Main menu"

    # Loading desativado para testes
    """ loading() """

    # Run the program loop
    while True:      
        clear()
        headers(HEADER)
        main_menu()  

        input_choice = get_int_input()

        if input_choice == None:
            continue
        
        choice = main_input_validated(input_choice)

        if choice is not int:
            continue

        if input_choice == 0:
            print_exit()
            break

        # Dispatch to the selected menu handler
        handler = routes.get(choice)
        if handler:
            handler()
        
    
if __name__ == "__main__":
    main()
    