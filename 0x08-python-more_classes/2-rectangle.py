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
    def width(self, width_value):
        """Set width"""
        if type(width_value) != int:
            raise TypeError("width must be an integer")
        if width_value < 0:
            raise ValueError("width must be >= 0")
        self.__width = width_value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value_height):
        """Set height"""
        if type(value_height) != int:
            raise TypeError("height must be an integer")
        if value_height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value_height

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2
