#!/usr/bin/python3
"""a class Student"""


class Student:
    """class method Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionnary representation"""
        return self.__dict__
