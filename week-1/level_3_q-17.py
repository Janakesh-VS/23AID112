import random
l=[]
for i in range (8):
    a=random.randint(1, 100)
    l.append(a)

max_num=l[0]
min_num=l[0]
for j in l:
    if j>max_num:
        max_num=j
    if j<min_num:
        min_num=j

print("The list is",l)
print("The biggest number is", max_num)
print("The smallest number is", min_num)