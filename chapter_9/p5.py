

with open("note.txt") as f:
    content=f.read()

with open("note_copy.txt","w")as f:
    f.write(content)
print("File copied successfully")