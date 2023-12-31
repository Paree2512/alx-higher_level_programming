#!/usr/bin/python3

"""Create class Square that inherits from `9-Rectangle`"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """initalizer
        Args
           size: size of side of square
        """
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
