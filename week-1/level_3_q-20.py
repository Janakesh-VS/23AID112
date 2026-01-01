list=[]
while True:
    print("1. Add")
    print("2. Remove")
    print("3. Show")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        n=input("Enter name of the item to be added:")
        list.append(n.upper())
    elif choice==2:
        n=input("Enter name of the item to be removed:")
        check=0
        for i in list:
            if i==n.upper():
                list.remove(i)
                check+=1
        if check==0:
            print("It is not found!")
            
    elif choice==3:
        print(list)
    elif choice==4:
        break
    else:
        print("Incorrect Choice!!")
        