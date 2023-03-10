
def _01(integers):
    sum = 0
    for x in integers:
        if x % 2 == 0:
            sum += x

    return sum