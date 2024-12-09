import random


computer = random.choice([-1,0,1])
youstr = input("Enter Your Choice: ")
youDict  = {"s":1,"w":-1,"g":0}
reverseDict  = {1:"snake",-1:"Water",0:"Gun"}
you = youDict[youstr]

print(f"You choose{reverseDict[you]}\n computer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("you lose!")

    elif(computer ==1 and you ==0):
        print("you win!")

    elif(computer == 0 and you == -1):
        print("you Win!")

    elif(computer ==0 and you ==1):
        print("You Lose!")

    else:
        print("something went wrong")