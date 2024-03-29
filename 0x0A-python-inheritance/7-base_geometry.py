#!/usr/bin/python3
"""defines a BaseGeometry class"""


class BaseGeometry:
    """Base Geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{}  must be greater than 0".format(name))
