word="donkey"
with open ("myfile.txt","r") as f:
    content =f.read()

contentNew=content.replace(word,"#####")


with open ("myfile.txt","w") as f:
    f.write(contentNew)