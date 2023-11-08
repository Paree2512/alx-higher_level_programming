#!/usr/bin/python3

"""
Module to create object from JSON file
Prototype: def load_from_json_file(filename):
You must use the with statement
"""

def load_from_json_file(filename):
    """
    Function that loads object from json file.
    Args:
        filename
    Return:
        object created from the file.
    """
    import json

    with open(filename) as obj_file:
        new_file = json.load(obj_file)
        return new_file
