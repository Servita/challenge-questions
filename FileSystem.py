#File System
#Write a program that accepts a file path and returns the number of words in the file.
def getWords(filePath):
    #Assumtpion that every word ends with a space or one of .!?
    with open(filePath,"r") as f:
        data = f.read()
        if len(data)==0 or len(data.strip(" "))==0:
            return(0)
        
        return(sum([1 if char==" " or char in ".!?" else 0 for char in data])+1)

def getWordsTest():
    for testCount in range(0,3):
        print(getWords("./testFile"+str(testCount+1)+".txt"))
    

getWordsTest()
#Write a program that accepts a directory path and returns the total size of all files in the directory.
#Write a program that accepts a directory path and returns the name of the file that has been modified most recently.