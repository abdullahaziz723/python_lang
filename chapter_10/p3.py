class demo:
    a=4


o=demo()
print(o.a)  # This will print the value of a, which is 4 ,class attribute

o.a=0 # This will change the value of a in the instance o, not the class attribute
print(o.a)  # This will print 0, as we have changed the value of a in the instance o
