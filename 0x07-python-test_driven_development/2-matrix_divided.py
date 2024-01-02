#!/usr/bin/python3
""" Module for matrix division """

def matrix_divided(matrix, div):
    """ Divides all matrix elements

    Args:
      matrix: the matrix to divide
      div: the number to divide the matrix by

    Returns:
      a new matrix

    Raises:
      TypeError: if matrix is not a list of lists of integers or floats
      TypeError: if Each row of the matrix is not of the same size
      TypeError: if div is not a number (integer or float)
      ZeroDivisionError: if div is equal to 0
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
