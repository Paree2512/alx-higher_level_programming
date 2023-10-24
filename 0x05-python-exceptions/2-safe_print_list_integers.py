#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        index = 0
        for y in range(x):
            if isinstance(my_list[y], int):
                index += 1
                print("{:d}".format(my_list[y]), end="")
    except TypeError:
        print("Type not an integer!")
    else:
        print("")
        return index
