#!/usr/bin/python3
""" Module to print_square method"""

def print_square(size):
    """Method for printing square

    Args:
       size: the size of square

    Raises:
      TypeError: if size is not an integer
      ValueError: if size is less than 0
      TypeError: if size is a float and is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
