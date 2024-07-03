import random


def generate_list(n: int, min_val: int, max_val: int) -> list:
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst
