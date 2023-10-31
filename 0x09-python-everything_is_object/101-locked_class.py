#!/usr/bin/python3

"""Locked Class Module"""

class LockedClass:
    """
    Class that prevents the user from dynamically
    creating any new instance attributes.
    """
    __slots__ = ('first_name')
    pass
