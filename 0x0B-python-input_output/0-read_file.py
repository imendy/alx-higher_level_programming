#!/usr/bin/python3
"""Read text file and prints to stdout"""


def read_file(filename=""):
    """Read text file (UTF8) and prints to stdout"""
    with open(filename, mode='r') as file:
        print(file.read(), end='')
