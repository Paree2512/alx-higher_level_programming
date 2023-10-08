#!/usr/bin/python3

def no_c(my_string):
    new_strng = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            new_strng += letter
    return new_strng
