class calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"{self.n*self.n}")


a=calculator(4)
a.square()  # This will call the square method