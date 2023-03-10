def secondSmallestInArray(array):
    if len(array) < 2:
        raise ValueError
    
    smallest = None
    secondSmallest = None

    for i in array:
        if smallest == None:
            smallest = i

        elif i < smallest:
            secondSmallest = smallest
            smallest = i

        elif secondSmallest == None:
            secondSmallest = i
        
        elif i > smallest and i < secondSmallest:
            secondSmallest = i

    return secondSmallest
  

# print(secondSmallestInArray((4, 3, 2, 1)))