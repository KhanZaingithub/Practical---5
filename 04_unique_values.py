def unique(list):
    unique_list = []

    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x,end=" ")        

list =[1,1,1,4,7,4,7,8,5]
print(" The unique values from list is ")
unique(list)
