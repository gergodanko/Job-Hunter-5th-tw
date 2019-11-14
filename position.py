from ui import *
from data_manager import *
#ID/description/no. of seats/company ID
def start_module():
    options=["Create position","Read position by id","Read all positions","Update position","Delete position"]
    table=import_data("position.txt")
    while True:
        print_menu("Positions",options,"Main menu")
        inputs=get_inputs("Please enter a number:","")
        option=inputs[0]
        if option=="1":
            create_position(table)
        elif option=="2":
            pos_id=get_inputs("Enter the position id: ","")
            print_result(read_position(table,pos_id),"")
        elif option=="3":
            print_result(read_positions(table),"")
        elif option=="4":
            print_result(update_positions(table),"")
        elif option=="5":
            print_result(delete_positions(table),"")
        elif option=="0":
            break
def create_position(table):
    new_position=[]
    new_position.append(generate_random(table))
    new_position.append(get_inputs("Type in the description: ",""))
    new_position.append(get_inputs("Type in the number of seats: ",""))
    new_position.append(get_inputs("Type in the company ID: ",""))
    export_data(new_position,"position.txt",mode="a")

    


def read_position(table,position_id):
    POS_ID=0
    data=[]
    applied=[]
    app_table=import_data("application.txt")
    stud_table=import_data("student.txt")
    for i in range(len(table)):
        if table[i][0]==position_id:
            data.append(table[i][1])
            data.append(table[i][2])
            data.append(table[i][3])
    for i in range(len(app_table)):
        if position_id==app_table[i][3]:
            for j in range(len(stud_table)):
                if app_table[i][2]==stud_table[j][0]:
                    applied.append([stud_table[j][0],stud_table[j][1]])
                    
    return data,applied

#print(read_position(import_data("position.txt"),"Ia'o24T'"))
                    



def read_positions(table):
    all_positions=[]
    POS_ID=0
    COMPANY_ID=3
    app_table=import_data("application.txt")
    for i in range(len(table)):
        seats_taken=0
        position=table[i]
        for j in range(len(app_table)):
            if app_table[j][3]==table[i][0]:
                if app_table[j][1]=="Yes":
                    seats_taken+=1
        position.append("{0}/{1}".format(table[i][2],seats_taken))
        all_positions.append(position)
    return all_positions

print(read_positions(import_data("position.txt")))

def update_positions(table):
    update_id=get_inputs("Type in the ID of the position you want to update: ","")
    row_no=0
    ID=0
    for i in range(len(table)):
        if table[i][ID]==update_id:
            row_no=i
            new_desc=get_inputs("Type in the new description: ","")
            table[i][1]=new_desc
    return table
#print(update_positions(import_data("position.txt")))



def delete_positions(table):
    app_table=import_data("application.txt")
    delete_id=get_inputs("Type in the ID of the position you want to delete: ","")
    row=0
    table2=[]
    for i in range(len(app_table)):
        if delete_id in app_table[i]:
            return "You can't delete this position"
        
    for i in range(len(table)):
        if table[i][0]==delete_id:
            row=i
    for j in range(len(table)):
        if j!=row:
            table2.append(table[j])
    return table2
#print(delete_positions(import_data("position.txt")))


