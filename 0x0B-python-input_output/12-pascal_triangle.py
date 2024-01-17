#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        T = triangle[-1]
        A = [1]
        for i in range(len(T) - 1):
            A.append(T[i] + T[i + 1])
        A.append(1)
        triangle.append(A)
    return triangle
