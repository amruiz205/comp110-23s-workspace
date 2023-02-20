


def max_number(number1: int, number2: int) -> int:
    """returns the maximum value out of two numbers"""
    if number1 >= number2:
        return number1
    else:
        return number2

my_max: int = max_number(1,10)
other_max_number: int = max_number(11, 3)
print(my_max)
print(other_max_number)
