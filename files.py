import os

def fileWords(fileName):
    file = open(fileName, "r")

    lines = file.readlines()

    words = 0

    for line in lines:
        line = line.split(" ")
        words += len(line)
        if(line == [''] or line == ['\n']):
            words += -1

    return words

def dirSize(directory):
    pass