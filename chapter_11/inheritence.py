class employee:
    name="deafult name"
    salary=10000
    def show (self):
        
         print (f"the name is {self.name} and the salaru is {self.salary}")


class programmer(employee):
     def show(self):
          print (f"the name is {self.name} and the salary is {self.salary}")


a=employee()
b=programmer()
b.show()    
