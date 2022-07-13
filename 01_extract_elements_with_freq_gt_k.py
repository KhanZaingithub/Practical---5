list = [4,6,4,3,3,4,3,7,8,8]
print(" The original list : "+ str(list))

k=2
res =[]
for i in list:
    freq = list.count(i)
    if freq > k and i not in res:
        res.append(i)

print(" The required elements : "+ str(res))
