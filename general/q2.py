def intersectionOfArrays(array1, array2):
    array1 = set(array1)
    array2 = set(array2)

    return tuple(array1 & array2)


# print(intersectionOfArrays([1, 2, 3, 4], [3, 4, 5, 6]))