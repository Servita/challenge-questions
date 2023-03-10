def secondSmallest(givenArray):
    if len(givenArray) == 0:
        return
    smallest = givenArray[0]
    for i in range(len(givenArray)):
        if givenArray[i] < smallest:
            smallest = givenArray[i]
    
    givenArray.remove(smallest)
    secondSmallest = givenArray[0]
    for i in range(len(givenArray)):
        if givenArray[i] < secondSmallest:
            secondSmallest = givenArray[i]

    return secondSmallest