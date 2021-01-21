#!/usr/bin/python3
"""Module description for Student"""


def pascal_triangle(n):
    """returns the pascal triangle"""
    triangle = []

    for i in range(0, n):
        row = []
        if i == 0:
            triangle.append([1])
            continue
        elif i == 1:
            triangle.append([1, 1])
            continue
        j = 0
        while j <= i + 1:
            if j > i:
                row.append(1)
                triangle.append(row)
                j += 1
                break
            elif (j - 1) < 0:
                row.append(1)
            else:
                if j < len(triangle[i - 1]):
                    row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
            j += 1
    return triangle
