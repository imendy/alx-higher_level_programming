#!/usr/bin/python3

"""
This is a module for a class Rectangle
"""


class Rectangle:
    """Class of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value_of_width):
        """Set width"""
        if type(value_of_width) != int:
            raise TypeError("width must be an integer")
        if value_of_width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value_of_width

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value_of_height):
        """Set height"""
        if type(value_of_height) != int:
            raise TypeError("height must be an integer")
        if value_of_height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value_of_height
