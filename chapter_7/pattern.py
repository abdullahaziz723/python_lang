
n= int(input("enter a number:"))
for i in range(1,1+n):
    print(" "*(n-i),end="")
    print("*"* (2*i-1),end="")
    print("")