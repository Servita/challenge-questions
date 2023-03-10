import os

def sizeOfFiles(path):
    totalSize = 0
    return os.path.getsize(path)



print(sizeOfFiles("files"))

# os.path.getmtime
# os.path.getsize