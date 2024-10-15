#!/usr/bin/python3
'''pascal_triangle'''


def pascal_triangle(n):
    """ returns a list of lists of integers representing the
    Pascal’s triangle of n """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tlr = triangles [-1]
        temp = [1]
        for i in range(len(tlr) - 1):
            temp.append(tlr[i] + tlr[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
