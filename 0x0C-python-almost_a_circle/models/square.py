#!/usr/bin/python3
"""Module for class square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constractor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints [Square] (<id>) <x>/<y> - <size>"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def sub_update(self, id=None, size=None, x=None, y=None):
        """sub method to update attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """a method to update attributes"""
        if args:
            self.sub_update(*args)
        elif kwargs:
            self.sub_update(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
