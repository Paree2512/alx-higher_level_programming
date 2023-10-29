#!/usr/bin/python3

"""
Printing Square.
The module prints a square using `#`.
"""


def print_square(size):
    """
    Function that prints a sqaure.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for x in range(size):
            print("#" * size)
