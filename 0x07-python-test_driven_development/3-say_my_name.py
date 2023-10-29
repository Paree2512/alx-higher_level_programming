#!/usr/bin/python3

"""
Say My Name module.
Raise exceptions if both names are not string types.
"""


def say_my_name(first_name, last_name=""):
    """Function that prints user's first name and last name."""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
