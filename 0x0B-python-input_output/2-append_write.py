#!/usr/bin/python3
"""Appends string to end of text file"""


def append_write(filename="", text=""):
    """Appends string to end of text file and
    return the number of characters written"""
    with open(filename, mode='a') as file:
        nchar = file.write(text)
        return nchar
