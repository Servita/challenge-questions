from typing import Any, List
def union_array_01(arr1: List[Any], arr2: List[Any]) -> List[Any]:
    return [x for x in arr1 if x in arr2] #O(n^2) ?

def union_array_02(arr1: List[Any], arr2: List[Any]) -> List[Any]:
    return list(set(arr1).intersection(set(arr2)))

def union_array_03(arr1: List[Any], arr2: List[Any]) -> List[Any]:
    common_dict = {item: True for item in arr1}
    return [x for x in arr2 if common_dict.get(x, False)] #O(n) ?