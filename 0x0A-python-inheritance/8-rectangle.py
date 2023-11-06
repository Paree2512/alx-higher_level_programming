#!/usr/bin/python3

"""Module based on `7-base_geometry`"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class Rectangle extends from BaseGeometry"""
    def __init__(self, width, height):
        """
        initializer
        Args:
            width
            height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
