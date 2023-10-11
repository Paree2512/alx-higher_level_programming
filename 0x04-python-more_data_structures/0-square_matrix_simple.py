#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for lists in matrix:
        new_ls = []
        for i in lists:
            new_ls.append(i ** 2)
        new_matrix.append(new_ls)

    return new_matrix
