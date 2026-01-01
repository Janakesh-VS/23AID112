sec_num=7

while True:
    guess=int(input("Guess the number:"))
    if guess>sec_num:
        print("Too high!")
    elif guess<sec_num:
        print("Too low!")
    else:
        print("You nailed it!")
        break