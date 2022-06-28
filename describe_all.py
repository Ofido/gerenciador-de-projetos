from os import listdir
from os.path import isfile

# isso fecha o arquivo sozinhos?
projects = [line.strip() for line in open('.config', 'r')]
arr = listdir()

for item in arr:
    if not isfile(item):
        if item not in projects:
            list_item = listdir(item)
            if ".git" in list_item:
                projects.append(item)