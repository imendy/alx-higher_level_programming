#!/usr/bin/python3
"""checks if the object is an instance of a class"""


def is_same_class(obj, a_class):
    """Function that determins if obj is an exact instance of a_class """
    if type(obj) is a_class:
        return True
    return False
