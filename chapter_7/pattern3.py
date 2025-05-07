

# * * *
# *   *
# * * * 

n =int(input("enter a number:"))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)  # First and last row
    else:
        print("*" + " " * (n - 2) + "*")  # Middle rows with spaces
