winning_number=18
num=int(input("enter the number between 1 and 50  :  "))
if num==winning_number:
    print("you win the game")
else:
    if num< winning_number:
        print("you are assuming too low")
    else:
        print("you are assuming too high")