def typecheck(arr):
    check = [type(el) == int for el in arr]
    if (all(check)):
        return True
    else:
        return "Invalid type. Please use a list of integers"

def total(arr):
    if typecheck(arr) == True:
        return sum(arr)
    else:
        return typecheck(arr)

def common(arr1, arr2):
    if typecheck(arr1) != True:
        return typecheck(arr1)
    elif typecheck(arr2) != True:
        return typecheck(arr2)
    else:
        result = []
        for el in max(arr1, arr2):
            if el in min(arr1, arr2):
                result.append(el)
            else:
                pass
        return result

def second_smallest(arr):
    if typecheck(arr) == True:
        arr.sort()
        return arr[1]
    else:
        return typecheck(arr)

def palindrome(string):
    try:
        s = [char for char in string]
    except:
        return "Invalid type. Please use a list of integers"
    else:
        if len(s) == 1 or len(s) == 0:
            return True
        elif len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        else:
            return s[0] == s[-1] and palindrome(string[1:-1])
    
def anagrams(string1, string2):
    try:
        s1 = [char for char in string1]
        s2 = [char for char in string2]
    except:
        return "Invalid type. Please use a list of integers"
    else:
        for char in s1:
            try:
                s2.remove(char)
            except:
                pass
        if len(s2) == 0:
            return True
        else:
            return False
    
print(anagrams("test", "ttes"))
print(anagrams(0, 1))
print(anagrams("abcba", "vbiukl"))
print(anagrams("a", "b"))
print(anagrams("aa", "aa"))
print(anagrams("ab", "ba"))
print(anagrams("abba", ""))