#!/usr/bin/python3

"""
Module that divides all integers within a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides the matrix """

    matrixError = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(matrixError)
    elif type(matrix) is not list:
        raise TypeError(matrixError)
    elif len(matrix) == 0:
        raise TypeError(matrixError)
    elif len(matrix[0]) == 0:
        raise TypeError(matrixError)

    final_matrix = []
    matrix_len = len(matrix[0])

    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(matrixError)
        if len(lists) != matrix_len:
            raise TypeError("Each row of the matrix must have the same size")

        newlist = []
        for x in lists:
            if not isinstance(x, (int, float)):
                raise TypeError(matrixError)
            newlist.append(round(x / div, 2))
        final_matrix.append(newlist)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif type(div) is bool:
        raise TypeError("div must be a number")
    elif type(div) is str:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return final_matrix
