def evenSumArray(array):
    sum = 0
    for i in array:
        if i % 2 == 0:
            sum += i
    return sum


# print(evenSumArray([1, 2, 3, 4, 5, 6]))