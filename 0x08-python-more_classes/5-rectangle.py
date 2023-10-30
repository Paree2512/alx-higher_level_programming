#!/usr/bin/python3

"""
Rectangle class that defines a rectangle from Module 4-rectangle
and expanding it to include being able to recognize and print a message if a rectangle is deleted.
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
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate area of rectangle based on valid widths and heights.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate perimeter of rectangle based on valid widths and heights.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print out rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""

        for r in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """String representation of rectangle to recreate new instance.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Detect if a rectangle is deleted and print a message.
        """
        print("Bye rectangle...")
