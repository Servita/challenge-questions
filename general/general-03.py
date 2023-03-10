from typing import List, Union
import math
def second_smallest(arr: List[int]) -> int:
    if len(arr) <= 1:
        raise ValueError("Given list too short")
    elif len(arr) == 2:
        return min(arr)

    smallest, second_smallest = math.inf, math.inf
    
    for value in arr:
        if value < smallest:
            second_smallest = smallest
            smallest = value
        elif value < second_smallest:
            second_smallest = value
    
    return second_smallest

# if 2 smallest are same, returns smallest. intentional functionality or bug?
print(second_smallest([2,2,3,4]))