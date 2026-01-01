a=input("Enter num1:")
b=input("Enter num2:")
a=int(a)
b=int(b)
s=a+b
d=a-b
p=a*b
print("The sum is",s)
print("The difference is",d)
print("The product is",p)
if a>b:
    print("num1 is greater!")
elif b>a:
    print("num2 is greater!")
else:
    print("Both are equal!")
