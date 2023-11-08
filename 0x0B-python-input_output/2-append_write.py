#!/usr/bin/python3

"""
Module that appends a string at the end of a text file(UTF8)
and return the number of characters added
Prototype: def append_write(filename="", text=""):
If the file doesn’t exist, it should be created
You must use the with statement
"""

def append_write(filename="", text=""):
    """
    Append string to end of text
    Args:
        filename
        text
    Return: number of characters added
    """
    with open(filename, 'a', encoding="UTF8") as myfile:
        content = myfile.write(text)
        return (content)
