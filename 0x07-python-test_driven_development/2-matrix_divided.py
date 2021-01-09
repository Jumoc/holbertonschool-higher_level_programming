#!/usr/bin/python3
"""This is the module description
    matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix and stores the result
        on another matrix
    Args:
        matrix: matrix to be divided
        div: number to divide the elements of the matrix
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    n_matrix = []
    size = None
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if size is not None and len(row) != size:
            raise TypeError("Each row of the matrix "
                            "must have the same size")
        size = len(row)
        n_row = []
        for col in row:
            if type(col) not in(int, float):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            n_row.append(round(col / div, 2))
        n_matrix.append(n_row)
    return n_matrix
