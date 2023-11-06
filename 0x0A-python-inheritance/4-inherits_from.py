#!/usr/bin/python3

"""
Creates a function that returns true if object is an
instance of a class that inherited from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Function checks if obj is an instance of a class
    inherited from a_class (directly or indirectly).
    Args:
        obj: object
        a_class: class

    Return: True or False
    """
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
