# guessing Game 
import random
n  =  random.randint(1,100)
a = -1
guesses = 0
while( a != n):
    guesses += 1      
    a= int(input("Guess a number:"))
    if(a > n):
        print("Lower Number please")
    else:
        print("Higher Number Please")

print(f"You have guessed the number correctly in {guesses} attempt")