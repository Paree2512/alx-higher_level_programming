#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = 0
    try:
        for y in range(x):
            print("{}".format(my_list[y]), end="")
            index += 1
    except IndexError:
        pass
    finally:
        print()
    return index
