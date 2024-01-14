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
        if list_dictionaries is None or not list_dictionaries:
            return []
        else:
            return dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_objs = [o.to_dictionnary() for o in list_objs]
        with open("{}.jason".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)
