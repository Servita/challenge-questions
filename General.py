# Q1
def sum_of_array(array):
    total = 0
    for elem in array:
        total += elem

    return total

# Q2
def same_elements(array1, array2):
    returnArray = []
    for elem1 in array1:
        for elem2 in array2:
            if elem1 == elem2:
                returnArray.append(elem1)

    return returnArray

# Q3
# def scnd_smallest(List array):
#     smallest = 0
#     for counter in range(2):
#         smallest = min(array)
#         array.remove()

# Q4
def is_palindrome(string):
    stringLength = len(string)
    for i in range(stringLength - 1):
        if string[i] != string[(stringLength - 1) - i]:
            return False

    return True


# print(sum_of_array([1,2,3]))
# print(same_elements((1,2,3), (1,2,4,3)))

# print(is_palindrome("tacocat"))

# Q5
