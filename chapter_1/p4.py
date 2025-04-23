import os

# Specify the directory (you can change this to any valid path)
directory_path = "/"  # "." means current directory

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
