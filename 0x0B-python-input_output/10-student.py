#!/usr/bin/python3
"""a class Student"""


class Student:
    """class method Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionnary representation"""
        try:
            for at in attrs:
                if type(at) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dictionnary = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionnary[key] = value
        return dictionnary
