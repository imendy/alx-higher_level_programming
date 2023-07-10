#!/usr/bin/python3
"""Create empty BaseGeometry class"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """Raise an exception with the specified message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value for int type."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
