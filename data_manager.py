def import_data(filename='albums_data.txt'):
    
    with open(filename, "r") as file_handle:
        lines = file_handle.readlines() 
    table=[]    
    for i in range(len(lines)):
        table.append([])
    table = [item.replace("\n", "").split(",") for item in lines]
    
    return table

def export_data(lst, filename, mode='a'):
    
    if mode!="w" and mode!="a":
        raise ValueError("Wrong write mode")
    
    with open(filename, mode) as file_handle:
        
            #row = ''.join(record)
        file_handle.write(",".join(lst)+ "\n")