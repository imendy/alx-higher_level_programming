#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math

class MagicClass:
    """Represent a circle."""

    def __init__(self, new_radius=0):
        """Initialize a MagicClass.

        Arg:
            new_radius (float or int): The radius of the new MagicClass.
        """
        self.__new_radius = 0
        if type(new_radius) is not int and type(new_radius) is not float:
            raise TypeError("radius must be a number")
        self.__new_radius = new_radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__new_radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return (2 * math.pi * self.__new_radius)
