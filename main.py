import ui

def choose():

def handle_menu():
    options=["Students","Company","Position","Application"]
    ui.print_menu("Main menu", options,"Exit program")
def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message
if __name__ == '__main__':
    main()