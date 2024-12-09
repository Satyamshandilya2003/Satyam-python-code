# a = "a very long string with emails"

# emails = []
# 3 seconds

f =  open("file.txt")
data = f.read()
print(data)
f.close()


# the same can be written usinf with statement like this 

with open("file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file   