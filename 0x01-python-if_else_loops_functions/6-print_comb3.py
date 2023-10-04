#!/usr/bin/python3

for n in range(0, 9):
    for n2 in range(n + 1, 10):
        if n == 8:
            print("{}{}".format(n, n2))
        else:
            print("{}{}, ".format(n, n2), end="")
