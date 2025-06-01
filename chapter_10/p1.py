class programmer:
    company = "Microsoft"

    def __init__(self, name, pin,salary):
        self.name=name
        self.pin=pin
        self.salary=salary

p=programmer("harry",110006,11200)
print(p.name,p.salary,p.pin)
print(p)