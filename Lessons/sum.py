"""example function for unit tests"""
# def sum(x: list[float]) -> float:
#     """return sum of all elements"""
#     sum_total: float = 0.0
#     i: int = 0
#     while i < len(x):
#         sum_total += x[i]
#         i += 1

#     return sum_total

#question 1
def sum(x: list[float]) -> float:
    """return sum of all elements"""
    sum_total: float = 0.0
    for i in range(len(x)):
        sum_total += x[i]

    return sum_total

#question 2
def sum(x: list[float]) -> float:
    """return sum of all elements"""
    sum_total: float = 0.0
    for i in range(0, len(x)):
        sum_total += x[i]

    return sum_total
