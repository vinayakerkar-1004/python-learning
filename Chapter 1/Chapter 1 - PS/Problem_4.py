import os

# specify the directory path
directory_path = "/Java"

# get the list of files and folders
entries = os.listdir(directory_path)

# print the contents
print("Contents of the directory:")
for entry in entries:
    print(entry)
