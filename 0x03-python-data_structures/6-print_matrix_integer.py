#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    num_row = len(matrix)

    for row in matrix:
        num_elements = len(row)
        col = 0

        for x in row:
            if col < num_elements - 1:
                print("{:d}".format(x), end=" ")
            else:
                print("{:d}".format(x), end="")
            col += 1
        print()
