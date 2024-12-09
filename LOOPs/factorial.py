#  5!  =  1x2x3x4x5

n = int(input("Enter The Number: "))
product  = 1
for i in range (1,n+1):
    product = product *i
print(f"The Factorial of{n} is {product}")