def numberOfWordsInFile(filename):
    with open(filename,"r") as f:
        return(len(f.readlines()))

print(numberOfWordsInFile("testdata.txt"))