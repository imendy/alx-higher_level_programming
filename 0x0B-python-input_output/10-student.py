#!/usr/bin/python3
"""A representation of a Student class"""


class Student:
    """Class that defines Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            dict = {}
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dict[attr] = self.__dict__[attr]
            return dict
        return self.__dict__
