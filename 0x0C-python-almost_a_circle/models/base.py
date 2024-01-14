#!/usr/bin/python3
"""Module for class Base"""
from json import dumps, loads

class Base:
    """The class Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Class constractor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        else:
            return dumps(list_dictionaries)
