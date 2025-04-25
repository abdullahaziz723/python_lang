#strings are immutable

name="abdullah"
ext=name[0:4]
print(ext)
print (name[-4:-1])  #==change to coresponding values =1,4
print(name[:4])  #start from -1 
print(name[1:])

str="the quick brown fox jumps over the lazy  dog"
print(str.replace("quick","fox"))
