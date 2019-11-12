def print_table(table,title_list):
    sizes=[]
    sum_of_sizes=0
    temp=1
    for i in range(len(table[0])):
        n=0
        for j in range(len(table)):
            if len(table[j][i])>n:
                n=len(table[j][i])
        if len(title_list[i])>n:
            n=len(title_list[i])
        sizes.append(n)
    size_pointer=0
    for size in sizes:
        sum_of_sizes+=size
    print("-"*(sum_of_sizes+(len(table[0]))+1))
    for word in title_list:
        if temp==len(title_list):
            print("|{0:^{1}}".format(word,sizes[size_pointer]), end="|\n")
        else:
            print("|{0:^{1}}".format(word,sizes[size_pointer]), end="")
        temp+=1
        size_pointer+=1
    print("-"*(sum_of_sizes+(len(table[0]))+1))
    
    
    for row in table:
        size_pointer=0
        temp=1
        for item in row:
            if temp==len(row):
                print("|{0:^{1}}".format(item,sizes[size_pointer]), end="|\n")
            else:
                print("|{0:^{1}}".format(item,sizes[size_pointer]) ,end="")
            size_pointer+=1
            temp+=1
        if temp==len(table[0]):
            print("-"*(sum_of_sizes+(len(table[0]))+1))
        else:
            print("|"+"-"*(sum_of_sizes+(len(table[0]))-1)+"|")


def print_result(result,label):
    print(result)
    print(label)

def print_menu(title,list_option,exit_message):
    print(title+":")
    counter=0
    for option in list_options:
        counter+=1
        print("\t"+"("+str(counter)+")" + option)
    print("\t(0)"+exit_message)

def get_inputs(list_labels, title):
    inputs = []
    inputs=input("".join(list_labels))
    return inputs

def print_error_message(message):
    print("An error occured!\n Error: "+message)