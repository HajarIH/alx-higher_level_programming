#!/usr/bin/python3
"""Module for test_indentattion method"""

def text_indentation(text):
    """Method that prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
      text: the text

    Raises:
      TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
