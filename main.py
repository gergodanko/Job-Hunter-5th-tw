import ui
import position
import student
import application
import company



def choose():
    inputs=ui.get_inputs("Please enter a number: ", "")
    option=inputs[0]
    if option=="1":
        student.start_module()
    elif option=="2":
        company.start_module()
    elif option=="3":
        position.start_module()
    elif option=="4":
        application.start_module()
    elif option =="0":
        quit()
    else:
        raise KeyError("There is no such option!")

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