l=[]
for i in range(1,21):
    l.append(i)

print("The list is",l)
print("The elements that are divisible by 3:")
for j in l:
    if j%3==0:
        print(j)