#!/usr/bin/python3
"""a class Rectangle"""

class Rectangle:
    """the class Rectangle"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing thr Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return ((str(self.print_symbol) * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle to be able to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
          rect_1: the first rectangle
          rect_2: the second rectangle

        Raises:
          TypeError: if rect_1 or rect_2 are not an instance of Rectangle

        Returns:
          The Rectangle with the larger area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def def square(cls, size=0):
        """a Rectangle where width == height == size

        Args:
          size: the size
        """
        return cls(size, size)
