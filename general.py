#### General
#1.  Create a function that accepts an array of integers and returns the sum of all the even numbers in the array.
def sumOfEven(array):
    return(sum([
        item if item%2==0 else 0 for item in array
    ]))

def sumOfEvenTest():
    print(sumOfEven([0,1,2,3]))#2
    print(sumOfEven([1,3,5]))#0
    print(sumOfEven([0,6,2,7]))#8

#sumOfEvenTest()

#2. Create a function that accepts two arrays and returns a new array that contains only the elements that are common between the two arrays.
def intersection(firstArray,secondArray):
    firstArray = set(firstArray)
    secondArray = set(secondArray)
    result = firstArray.intersection(secondArray)
    result = list(result)
    return(result)

def intersectionTest():
    print(intersection([1,2,3],[4,5,6]))#[]
    print(intersection([1,2,3],[1,2,3]))#[1,2,3]
    print(intersection([1,2,3],[1,3,4]))#[1,3]
    print(intersection([1,2,3],[6,2,2]))#[2]

#intersectionTest()

#3. Create a function that accepts an array of integers and returns the second smallest number in the array.
def secondSmallest(array):
    if len(array)==0:
        return()
    smallest = min(array)
    second_smallest = max(array)
    if second_smallest==smallest:
        return()
    
    
    for item in array:
        if item!=smallest and second_smallest>item:
            second_smallest = item
    
    
    return(second_smallest)

def secondSmallestTest():
    print(secondSmallest([]))#[]
    print(secondSmallest([0,0,0]))#[]
    print(secondSmallest([0,1,0]))#1
    print(secondSmallest([0,1,2,3]))#1
    print(secondSmallest([4,1,8,3]))#3

#secondSmallestTest()

#4. Write a program that accepts a string and returns true if the string is a palindrome, false otherwise.
def isPalindrome(word):
    return(word.lower()==(word.lower())[::-1])

def isPalindromeTest():
    print(isPalindrome("Hi"))#False
    print(isPalindrome("palindrome"))#False
    print(isPalindrome("racecar"))#True
    print(isPalindrome("raceecar"))#True
    print(isPalindrome(""))#True

#isPalindromeTest()

#5. Write a program that accepts two strings and returns true if they are anagrams of each other, false otherwise.
def isAnagram(firstWord,secondWord):
    if len(firstWord)!=len(secondWord):
        return(False)
    elif firstWord!=secondWord:
        letterDict = {}
        for firstWordLetter,secondWordLetter in zip(firstWord,secondWord):
            if firstWordLetter in letterDict.keys():
                letterDict[firstWordLetter]+=1
            else:
                letterDict[firstWordLetter]=1
        
            if secondWordLetter in letterDict.keys():
                letterDict[secondWordLetter]-=1
            else:
                letterDict[secondWordLetter]=-1
    
        for key in letterDict.keys():
            if letterDict[key]!=0:
                return(False)
    
    return(True)


def isAnagramTest():
    print(isAnagram("abc","def"))#False
    print(isAnagram("abc","abc"))#True
    print(isAnagram("abc","cba"))#True
    print(isAnagram("",""))#True
    print(isAnagram("abcd","cba"))#False
    print(isAnagram("abcd","cb a"))#False

#isAnagramTest()
