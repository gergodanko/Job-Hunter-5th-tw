from ui import *
from data_manager import *
from student import *
from position import *

def create_application(table):
    application_list = []
    application_list.append(generate_random(table))
    application_list.append(get_inputs("Accepted?: ", ""))
    application_list.append(get_inputs("Enter the student ID: ", ""))
    application_list.append(get_inputs("Enter the Position ID: ", ""))
    export_data(application_list,"application.txt","a")


create_application(import_data("application.txt"))