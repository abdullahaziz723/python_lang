class employee:
    a=1

    
    @classmethod
    def show(self):
        print(f"the value of a is {self.a}")

e=employee()    
e.a=45

e.show()  # This will print "the value of a is 45" because we changed the instance attribute a
