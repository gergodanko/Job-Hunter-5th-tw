from ui import *
from data_manager import *
#from student import *
from position import *
def start_module():
    options=["Create an application", "Update an application","Delete an application"]
    table=import_data("application.txt")
    while True:
        print_menu("Applications", options,"Main menu")
        inputs=get_inputs("Please enter a number: ", "")
        option=inputs[0]
        if option=="1":
            create_application(table)
        elif option=="2":
            print_result(update_application(table),"")
        elif option=="3":
            print_result(delete_application(table))
        elif option=="0":
            break

        
def create_application(table):
    application_list = []
    application_list.append(generate_random(table))
    application_list.append(get_inputs("Accepted?: ", ""))
    application_list.append(get_inputs("Enter the student ID: ", ""))
    application_list.append(get_inputs("Enter the Position ID: ", ""))
    export_data(application_list,"application.txt","a")

def update_application(table):
    update_acc=get_inputs("Type in the ID of the application you want to update: ","")
    row_no=0
    ID=0
    for i in range(len(table)):
        if table[i][ID]==update_acc:
            row_no=i
            new_stat=get_inputs("Accepted? (Yes/No) : ","")
            table[i][1]=new_stat
    return table
#print(update_application(import_data("application.txt")))
def delete_application(table):
    delete_id=get_inputs("Type in the ID of the application you want to delete: ","")
    row=0
    table2=[]
    for i in range(len(table)):
        if table[i][0]==delete_id:
            row=i
    for j in range(len(table)):
        if j!=row:
            table2.append(table[j])
    return table2

