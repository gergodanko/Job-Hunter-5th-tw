from ui import *
from data_manager import *

def start_module():
    options=["Create company","Read company","Read companies","Update company","Delete company"]
    table=import_data("position.txt")
    while True:
        print_menu("Positions",options,"Main menu")
        inputs=get_inputs("Please enter a number:","")
        option=inputs[0]
        if option=="1":
            create_company(table)
        elif option=="2":
            print_result(read_company(import_data("company.txt"),import_data("position.txt")),"")
        elif option == "3":
            print_result(read_companies(import_data("company.txt")),"")
        elif option == "4":
            print_result((update_company(import_data("company.txt"))),"")
        elif option == "5":
            print_result((delete_company(import_data("company.txt"))),"")
        elif option=="0":
            break

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


def read_company(table,table1):
    show_list = []
    show_id = get_inputs("Give ID: ", "")
    for i in range(len(table)):
        if show_id in  table[i]:
            show_list.append(table[i][0])
            show_list.append(table[i][1])
    for j in range (len(table1)):
        if show_id in table1[j]:
            show_list.append(table1[j][0])
            show_list.append(table1[j][1])
            show_list.append(table1[j][2])
    return show_list

def read_companies(table):
    show_all = []
    for i in range(len(table)):
        show_all.append(table[i][0])
        show_all.append(table[i][1])
 
 
    #print(",".join(show_all))

    return show_all


def update_company(table):
    entered_id = get_inputs("Enter the ID you want to update: ", "")
    for i in range(len(table)):
        if entered_id == table[i][0]:
            table[i].pop(1)
            new_name = get_inputs("Enter the new name: ", "")
            table[i].append(new_name)
    #for i in range(len(table)): 
    #    export_data(table[i],"company.txt","w")
    return table

def delete_company(table):
   
    enter_id = get_inputs("Please enter the ID: ", "")
    app_table = import_data("application.txt")
    pos_table = import_data("position.txt")
    pos_id=""
    count = 0
    for i in range(len(pos_table)):
        if enter_id == pos_table[i][3]:
            pos_id=pos_table[i][0]
            pos_seats=pos_table[i][2]
            for j in range(len(app_table)):
                if app_table[j][3]==pos_id:
                    if app_table[j][1]=='Yes':
                        count+=1

    if int(pos_seats)!=count:
        return "You can't delete this company!"
    else :
        x_genyo = 0
        for j in range(len(table)):
            if enter_id == table[j][0]:
                x_genyo = j
        table.pop(x_genyo)
        return table
                     
                







#print(delete_company(import_data("company.txt")))
    


#print(read_company(import_data("company.txt"),import_data("position.txt")))


#print(print_multiple_files(import_data("company.txt"),import_data("position.txt")))


#print(read_companies(import_data("company.txt")))
#print(update_company(import_data("company.txt")))





#print(create_company(import_data("company.txt")))



