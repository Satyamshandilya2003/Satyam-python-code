cities =  ["Delhi","Gurgaon","Pune","Muzaffarpur","Chennai"]
heroes = ["satyam","Iroman","Batman","Shaktiman"]

print(heroes[0],end="  ")
print(heroes[1],end=" ")

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_len(cities)
print_len(heroes)