def areAnagrams(string1, string2):
    # Returns true if string 1 can be rearranged to make string 2
    letters = list(string1)

    # Go through string 2, see if you have the letters to make it
    for i in string2:
        if i in letters:
            # Remove character
            letters.remove(i)

        else:
            return False
    
    return True


print(areAnagrams("hannah", "hannah"))