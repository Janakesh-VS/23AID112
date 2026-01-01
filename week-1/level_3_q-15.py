list = [12, 45, 3, 98, 7, 34, 21]
c=0
print("Elements of list:")
for i in list:
    print(i)

print("Elements greater than 30:")
for j in list:
    if j>30:
        print(j)
        c+=1
print("No.of elements greater than 30:",c)    