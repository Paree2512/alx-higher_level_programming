#!/usr/bin/python3

"""
Text Indentation module.
This module adds two new lines after these characters: ".?:".
Raise exceptions if text is not a string.
"""


def text_indentation(text):
    """Function that prints 2 new lines"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # initialize variable to hold final text
    final_text = ""

    # skip/trim leading whitespaces
    trim_spaces = True

    # iterate through all chars in the text
    for char in text:
        if char in ".?:":
            final_text += char + "\n\n"
            trim_spaces = True
        elif char != " " or not trim_spaces:
            final_text += char
            trim_spaces = False

    print(final_text)
