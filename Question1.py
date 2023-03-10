import numpy as np
import array
def sumEvenArray(arr):
    output = 0
    for i in arr:
        if i % 2 == 0:
            output += i
    return output

def sumCommonArray(arr1, arr2):
    output = 0
    for i in arr1:
        for j in arr2:
            if i == j:
                output += i
    return output

def secondSmallest(arr):
    smallest = np.min(arr)
    arr.pop(smallest)
    smallest = np.min(arr) 
    return smallest
