#!/usr/bin/python3

"""Function that checks if an object is of a certain class"""

def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of a_class
    Args:
        obj: object
        a_class: class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
