def numWordsInFile(path):
    with open(path, "r") as txtfile:
        # Read data
        data = txtfile.read()
        # Replace newlines with spaces, stripping extra spaces
        data = data.replace("\n", " ").strip()
        data = data.split(" ")
    
    return len(data)


print(numWordsInFile("files\\testfile.txt"))