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
