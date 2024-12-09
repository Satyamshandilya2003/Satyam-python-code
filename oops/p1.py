class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Satyam", 12000000, 18001)
print(p.name, p.salary, p.pin)
r  =  Programmer("Harry",120000,180002)
print(r.name,r.salary,r.pin)

s = Programmer("richa",234556,12220)
print(s.name,s.salary,s.pin)