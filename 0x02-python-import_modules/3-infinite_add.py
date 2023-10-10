#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0
    arg_count = len(sys.argv) - 1

    for i in range(arg_count):
        result += (int(sys.argv[i + 1]))
    print("{:d}".format(result))
