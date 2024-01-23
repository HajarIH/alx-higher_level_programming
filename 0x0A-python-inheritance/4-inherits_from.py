#!/usr/bin/python3
"""inherits from"""


def inherits_from(obj, a_class):
    """ a function that returns True if the object is an
    instance of a class that inherited 
    from the specified class ; otherwise False"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
