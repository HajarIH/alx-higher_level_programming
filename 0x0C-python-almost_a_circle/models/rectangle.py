#!/usr/bin/python3
"""Module for class Rectangle"""
from models.base import Base

class Rectangle(Base):
    """a class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constractor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate("heigth", value, False)
        self.__height = value

    @property
    def x(self):
        """x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate("x", value, True)
        self.__x = value

    @property
    def y(self):
        """y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate("y", value)
        self.__y = value

    def validate(self, name, value, equality=True):
        """validation of setter methods"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if equality and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not equality and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def display(self):
        """Method that prints rectangle"""
        print("\n" * self.y + (" " * self.x + "#" * self.width+ "\n") * self.height, end="")

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.x, self.y, self.width, self.height) 

    def sub_update(self, id=None, width=None, height=None, x=None, y=None):
        """sub method to update attributes"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
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
