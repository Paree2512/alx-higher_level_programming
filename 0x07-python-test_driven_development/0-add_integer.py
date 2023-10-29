#!/usr/bin/python3

"""
A function that adds two integers/float.
Returns an integer: the sum of a and b
"""


def add_integer(a, b=98):
    """
    Function adds two integers with the second argument being optional.
    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    Returns:
        int: The addition of `a` and `b` as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # cast numbers into integers if they are float
    a = int(a)
    b = int(b)

    return int(a) + int(b)
