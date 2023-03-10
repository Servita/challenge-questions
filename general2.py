def commonElements(array1, array2):
    common = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                common.append(array1[i])
    
    return common