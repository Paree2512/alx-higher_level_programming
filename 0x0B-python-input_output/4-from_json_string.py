#!/usr/bin/python3

"""
Module to return an object represented by a JSON string:
Prototype: def from_json_string(my_str):
"""

def from_json_string(my_str):
    """
    Function to convert a JSON string to a Python object (data structure).
    Args:
        my_str: The JSON string to be deserialized.
    Return:
        object: the python object represented by the JSON string.
    """
    import json

    data_str = json.loads(my_str)
    return (data_str)
