def palindrome(givenString):
    for i in range(int(len(givenString)/2)):
        if givenString[i] != givenString[len(givenString)-1-i]:
            return False

    return True