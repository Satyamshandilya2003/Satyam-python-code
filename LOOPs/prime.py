n =  int(input("enter number whom you want to check : "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
    else:
        print("number is prime")