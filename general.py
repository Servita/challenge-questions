def addInts(intArray):
    total = 0

    for integer in intArray:
        total += integer

    return total

def arrayIntersection(arrayA, arrayB):
    returnArray = []

    for i in arrayA:
        if(i in arrayB):
            returnArray.append(i)
            arrayB.remove(i)
            continue
    
    return returnArray

def secondSmallest(intArray):
    smallests = [intArray[0], intArray[0]]

    for i in intArray:
        if(i < smallests[0]):
            smallests[0], smallests[1] = i, smallests[0]
    
    if(smallests[0] == smallests[1]):
        return secondSmallest(intArray[1:] + [intArray[0]])
    
    return smallests[1]

def isPalindrome(palindrome):
    for i in range(0, len(palindrome) // 2):
        if(palindrome[i] != palindrome[len(palindrome) - 1 - i]):
            return False
    
    return True

def isAnagram(wordA, wordB):
    wordA = wordA.lower()
    wordB = wordB.lower()

    stringArray = []

    for i in wordA:
        stringArray.add(i)
    
    for i in wordB:
        if(i in stringArray):
            stringArray.remove(i)
        else:
            return False
    
    return len(stringArray) == 0
