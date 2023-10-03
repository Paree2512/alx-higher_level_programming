#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
            result += char
            print(result)
