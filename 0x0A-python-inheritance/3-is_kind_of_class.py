#!/usr/bin/python3

"""Check if an object is a class or sub class"""

def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a class inherited from a_class.
    Args:
        obj: object
        a_class: class
    Return: True or False
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
