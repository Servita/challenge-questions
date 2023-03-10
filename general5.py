def anagrams(string1,string2):
    if len(string1) != len(string2):
        return False
    letters = []
    for i in range(len(string1)):
        letters.append(string1[i])
    
    for i in range(len(string2)):
        if string2[i] not in letters:
            return False
        else:
            letters.remove(string2[i])
    return True
