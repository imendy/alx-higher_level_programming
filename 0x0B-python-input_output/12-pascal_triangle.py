#!/usr/bin/python3

"""Defines a Pascal's triangle function"""


def pascal_triangle(n):
    """
    returns a list of lists of
    integers representing the Pascals triangle of n
    """
    p_triangle = [[1], [1, 1]]

    if n <= 0:
        return []

    if n == 1:
        return [p_triangle[0]]

    for i in range(n-2):
        base = p_triangle[-1]
        part = []
        part.append(base[0])
        for j in range(len(base)):
            if j < (len(base) - 1):
                part.append(base[j] + base[j + 1])
        part.append(base[-1])
        p_triangle.append(part)

    return p_triangle
