#!/usr/bin/python3
"""writing file with 2 arguments"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8) """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
