from ui import *
from data_manager import *

def print_multiple_files(table1,table2):
    merge=[]
    merge.append(table1)
    merge.append(table2)
    return merge
    #export_data(position_data, "position.txt", "a")
        
def create_company(table):
    company_list = []
    create_id = generate_random(table)
    create_name = get_inputs("Type in the name: ", "")
    company_list.append(create_id)
    company_list.append(create_name)
    

    export_data(company_list,"company.txt", mode= "a")
    return company_list


def read_company(table):
    show_list = []
    show_id = get_inputs("Give ID: ", "")
    for i in range(len(table)):
        if show_id == table[i]:
            show_list.append(table[i])
    return show_id


#print(read_company(import_data("company.txt")))


print(print_multiple_files(import_data("company.txt"),import_data("position.txt")))









print(create_company(import_data("company.txt")))



