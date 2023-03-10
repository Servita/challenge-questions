def sum_even(n: int) -> int:
    return sum(x for x in range(n) if x % 2 == 0)