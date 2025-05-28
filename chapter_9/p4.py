

with open("note.txt")as f:
    content=f.read()


if("python"in content):
    print("yes")
else:
    print("no")