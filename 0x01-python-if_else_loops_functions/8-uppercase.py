#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        val = ord(ch)
        flag = 0

        if val >= 97 and val <= 122:
            flag = 32

            print("{}".format(chr(val - flag)), end="")

            print()
