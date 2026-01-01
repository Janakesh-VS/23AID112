grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
c1=c2=c3=c4=0

for i in grades:
    if i>=90:
        c1+=1
    elif i>=80:
        c2+=1 
    elif i>=70:
        c3+=1 
    else:
        c4+=1 

print("No.of students who got more than or equal to 90",c1)
print("No.of students who got more than or equal to 80",c2)
print("No.of students who got more than or equal to 70",c3)
print("No.of students who got less than 70",c4)