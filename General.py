import math
def sum_even_array(array):
    total = 0 
    for number in array:
        if number%2 == 0:
            total+=number
    return total

def common_items(array_one,array_two):
    output_array=common_items(array_one,array_two)
    return output_array

def second_smallest(array):
    array.sort()
    return array[1]


def is_palindrome(word):
    start=0
    for i in range(start, ((len(word)//2)+1)):
        if word[i] != word[-i-1]:
            return False
    return True

def is_anagram(word_one,word_two):
    letters=[]
    for char in word_one:
        letters.append(char)
    for character in word_two:
        if character in letters:
            letters.pop(character)
    if letters == []:
        return True
    else:
        return False
