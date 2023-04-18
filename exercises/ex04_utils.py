"""List utility functions!"""
__author__ = "730599859"


def all(x: list[int], y: int) -> bool:
    """This function returns a bool if y is equal to every index of x!"""
    if len(x) == 0:
        return False
    i: int = 0
    while len(x) > i:
        if x[i] == y:
            i += 1
        else:
            return False
    return True


def max(x: list[int]) -> int:
    """This function looks through a list and returns the highest integer in the list!"""
    if len(x) == 0:
        raise ValueError("max() arg is an empty list")
   
    else:
        maximum1: int = 0
        maximum2: int = 0
        maximum: int = 0
        c: int = 0
        idx: int = 0
        y: int = 1

        while c < len(x) * 2 and idx != len(x) and y != len(x):
           
            if x[idx] >= x[y]:
                maximum1 = x[idx]
                y = y + 1

            else:
                maximum2 = x[y]
                idx = idx + 1
            c += 1

        if maximum1 >= maximum2:
            maximum = maximum1

        elif maximum2 > maximum1:
            maximum = maximum2

    return maximum


def is_equal(x: list[int], y: list[int]) -> bool:
    """This function checks if the two lists are equal at each index!"""
    idx = 0

    if len(x) == 0 and len(y) == 0:
        return True
   
    elif len(x) == 0 or len(y) == 0:
        return False
   
    while idx < len(x) and len(x) == len(y):
        if x[idx] == y[idx]:
            idx += 1
        else:
            return False
       
    if len(x) != len(y):
        return False
    else:
        return True
       