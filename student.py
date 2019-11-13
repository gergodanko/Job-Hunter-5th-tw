from ui import *
from data_manager import *


        
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







print(create_student(import_data("student.txt")))



