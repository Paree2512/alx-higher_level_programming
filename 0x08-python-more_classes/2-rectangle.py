#!/usr/bin/python3

"""
Rectangle class that defines a rectangle by private 
instance attribute: width and height.
"""

class Rectangle:
    """
    Variables instantiation of width and height

    Args:
        width (int)
        height (int)
    """
    def __init__(self, width=0, height=0):
        # initialize private attributes
        self.__width = width
        self.__height = height

    @property
    def width(self):
        # property to retrive width
        return self.__width

    @width.setter  # setter method for width
    def width(self, value):
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        # update private instance attribute
        self.__width = value

    @property
    def height(self):
        # property to retrive height
        return self.__height

    @height.setter  # setter method for height
    def height(self, value):
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        # update private instance attribute
        self.__height = value

    def area(self):
        """
        Calculate the area of rectangle based on valid
        widths and heights.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of rectangle based on valid
        widths and heights.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
