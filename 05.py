def _05(first, second):
    return sorted(first) == sorted(second)

print(_05("email", "laime")) # true
print(_05("email", "laimee")) # false
print(_05("emaeil", "laimee")) # true