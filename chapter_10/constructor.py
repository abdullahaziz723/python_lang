class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self): # dunder method which is automatically called
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")



harry=Employee() # This will call the __init__ method   
harry.getInfo() # This will call the getInfo method
harry.name = "Harry" # This will create an instance attribute
print(harry.salary) # This will print the class attribute language
