def isPalindrome(inputString):
    inputString = inputString.lower().strip()
    if inputString == inputString[::-1]:
        return True
    else:
        return False
    

#print(isPalindrome("hannah"))