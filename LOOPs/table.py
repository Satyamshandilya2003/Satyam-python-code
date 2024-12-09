# number = int(input("Enter Number Whose Table You Want :"))
# i = 1
# while i<=10:
#     print (number*i)
#     i  +=1


number = int(input("Enter Number Whose Table You Want: "))
for i in range(1, 11):  # Multiplication table from 1 to 10
    result = number * i
    print(f"{number} x {i} = {result}")
