#!/usr/bin/python3
"""a class Rectangle"""

class Rectangle:
    """the class Rectangle"""
    def __init__(self, width=0, height=0):
        """initializing thr Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """the private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints string representation of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for j in range(self.__height))

    def __repr__(self):
        """ return a string representation of the rectangle to be able to recreate a new instance"""
        return "Rectangle({:d},{:d})".format(self.__width, self.__height)
