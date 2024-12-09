import os

# Create 'tables' folder if it doesn't exist
os.makedirs('tables', exist_ok=True)

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n}X{i} = {n*i}\n"
    
    # Save the file in the 'tables' folder
    with open(f"tables/tables_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)
