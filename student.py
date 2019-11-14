from ui import *
from data_manager import *


def start_module():
    options=["Create student","Read student by id","Read all students","Update student","Delete student","Activate / Deactivate Student"]
    table=import_data("student.txt")
    while True:
        print_menu("Students",options,"Main menu")
        inputs=get_inputs("Please enter a number:","")
        option=inputs[0]
        if option=="1":
            create_student(table)
        elif option=="2":
            stud_id=get_inputs("Enter the student id: ","")
            print_result(read_student(table,stud_id),"")
        elif option=="3":
            print_result(read_students(table),"")
        elif option=="4":
            print_result(update_student(table),"")
        elif option=="5":
           print_result(delete_student(table),"")
        elif option=="6":
            print_result(act_deact_stud(table),"")
        elif option=="0":
            break


def create_student(table):
    student_list = []
    student_id = generate_random(table)
    student_name = get_inputs("Student's name: ", "")
    student_age = get_inputs("Student's age: ", "")
    student_sub = get_inputs("Is the student Active(1) or Not(0): ", "")
    student_list.append(student_id)
    student_list.append(student_name)
    student_list.append(student_age)
    student_list.append(student_sub)
    

    export_data(student_list,"student.txt", mode= "a")
    return student_list


def read_student(table, id):
    showlist = []
    app_table = import_data("application.txt")
    for lines in table:
        if lines[0] == id:
            showlist.append(lines[1])
            showlist.append(lines[2])
            for lines in app_table:
                if lines[2] == id:
                    showlist.append(lines[0])
            return showlist

def read_students(table):
    showlist = []
    for lines in table:
        showlist.append(lines[0])
        showlist.append(lines[1])
    
    return showlist

def update_student(table):
    update_id=get_inputs("Type in ID of student: ","")
    row_no=0
    ID=0
    for i in range(len(table)):
        if table[i][ID]==update_id:
            row_no=i
            new_name=get_inputs("Type in name: ","")
            new_age=get_inputs("Type in age: ","")
            table[i][1]=new_name
            table[i][2]=new_age
    return table

def act_deact_stud(table):
    stud_id = get_inputs('Enter the student id: ',"")
    row_no = 0
    ID = 0
    for i in range(len(table)):
        if table[i][ID]==stud_id:
            row_no=i
            newact=get_inputs("Active(1) or Deactivate(0): ","")
            table[i][3]=newact
        return table

def delete_student(table):
    app_table=import_data("application.txt")
    delete_stud=get_inputs("Enter the student id: ","")
    row=0
    table2=[]
    for i in range(len(app_table)):
        if delete_stud in app_table[i]:
            return "Student can't be deleted with existing application"
        
    for i in range(len(table)):
        if table[i][0]==delete_stud:
            row=i
    for j in range(len(table)):
        if j!=row:
            table2.append(table[j])
    return table2


