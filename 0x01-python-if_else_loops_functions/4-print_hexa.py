#!/usr/bin/python3

for num in range(0, 99):
    if num == 113 or num == 101:
        continue
    print("{} = {}".format(num, hex(num)))
