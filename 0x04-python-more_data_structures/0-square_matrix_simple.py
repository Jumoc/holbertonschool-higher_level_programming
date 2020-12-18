#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for row in matrix:
        elements = []
        for element in row:
            elements.append(element ** 2)
        new_mat.append(elements)
    return new_mat
