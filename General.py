def sumEvenNumbers(arr):
    '''accepts an array of integers and returns the sum of all the even numbers in the array
        ARGS - arr: array of integers
        RETURNS- sum of all even numbers: int'''
    return sum(filter(lambda x: x%2 == 0,arr))

def commonElements(arr1,arr2):
    '''function that accepts two arrays and returns a new array that contains only the elements that are common between the two arrays'''
    return list(set(arr1).intersection(set(arr2)))

def secondSmallestInArray(arr):
    '''function that accepts an array of integers and returns the second smallest number in the array.'''    
    arr.sort()
    return(arr[1])

def palindromeChecker(string):
    '''accepts a string and returns true if the string is a palindrome, false otherwise.'''
    if string == string[::-1]:return True
    return False

def anagramChecker(str1,str2):
    '''accepts two strings and returns true if they are anagrams of each other, false otherwise'''
    if len(str1) == len(str2):
        arr1,arr2 = [],[]
        for char in str1:
            arr1.append(char)
        for char in str2:
            arr2.append(char)
        arr1.sort()
        arr2.sort()
        for index,char in enumerate(arr1):
            if arr2[index] != char:
                break
        else:
            return True
    return False
    


        

