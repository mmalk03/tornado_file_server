import os

f = []

path = os.getcwd() + '/uploads'
for (root, directories, file_names) in os.walk(path):
    for file_name in file_names:
        f.append(file_name)

print(f)
