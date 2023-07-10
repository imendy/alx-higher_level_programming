#!/usr/bin/python3
"""
Contains definition of class Reactangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definifition of class Rectangle that inherits from BaseGeometry.
       Attributes:
            width (int): width of the rectangle.
            height (int) height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes an instance of class Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width

        self.__height = height

    def area(self):
        """Returns are of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """
        Returns string representation of an instance of class rectangle
        """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
