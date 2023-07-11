#!/usr/bin/python3
"""Write string to a text file"""


def write_file(filename="", text=""):
    """Write string to a text file and
    return the number of characters written"""
    with open(filename, mode='w') as file:
        nchar = file.write(text)
        return nchar
