"""List utility functions!"""
__author__ = "730599859"


def only_evens(x: list[int]) -> list[int]:
    """Takes a list and returns the evens!"""
    evens: list[int] = list()
    for i in x:
        if i % 2 == 0:
            evens.append(i)
    return evens


def concat(x: list[int], y: list[int]) -> list[int]:
    """Concats 2 input lists."""
    concat_list: list[int] = list()
    for i in x:
        concat_list.append(i)
    for i in y:
        concat_list.append(i)
    return concat_list


def sub(x: list[int], y: int, z: int) -> list[int]:
    """Defines a sub function."""
    sub_list: list[int] = list()
    if len(x) == 0 or y >= len(x) or z <= 0:
        return sub_list
    else:
        i: int = y
        max: int = z
        if y < 0:
            i = 0
        if z > len(x):
            max = len(x)
        while i < max:
            sub_list.append(x[i])
            i += 1
    return sub_list
