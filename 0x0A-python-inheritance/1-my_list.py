#!/usr/bin/python3
"""a module to define MyList class"""


class MyList(list):
    """a class list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
