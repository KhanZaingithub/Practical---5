list1 = [8,15,14]
list2 =[5,9,7]

multiplied = list()
for item1,item2 in zip(list1,list2):
    item = item1 * item2
    multiplied.append(item)

print(multiplied)  