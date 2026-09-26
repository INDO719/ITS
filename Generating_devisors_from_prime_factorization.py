from math import prod
from itertools import permutations


def f(n: int) -> list:
    if n == 1: return []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f(n // i) + [i]
    return [n]


def div(simple_numbers: list) -> list:
    result = set()

    for x in range(len(simple_numbers)):
        list_of_variation = [prod(y) for y in permutations(simple_numbers, r=x + 1)]
        for i in list_of_variation:
            result.add(i)
    return [1] + list(result)
