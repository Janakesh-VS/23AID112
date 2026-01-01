light=input("Enter current light status:")
if light.upper()=="RED":
    print("STOP!")
elif light.upper()=="YELLOW":
    print("Prepare to stop")
elif light.upper()=="GREEN":
    print("You can go")
else:
    print("Wrong input!")