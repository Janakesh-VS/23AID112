temp_in_cel=float(input("Enter the temperature:"))
temp=(temp_in_cel*9/5)+32
if temp_in_cel <0:
    print("Very cold! Wear thick jacket")
elif temp_in_cel<16:
    print( "Cold. Wear jacket")
elif temp_in_cel<26:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")