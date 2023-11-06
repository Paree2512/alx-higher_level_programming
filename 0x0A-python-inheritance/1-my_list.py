#!/usr/bin/python3

"""Class definition for MyList"""

class MyList(list):
    """MyList inherits from the list class"""

    def __init__(self):
        """initializer for MyList"""
        super().__init__()

    def print_sorted(self):
        """prints the list(sorted) in ascending order
        type(int)
        """
        print(sorted(self))
