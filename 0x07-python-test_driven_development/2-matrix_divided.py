#!/usr/bin/python3
"""Module for matrix_divided function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div
    rounded to 2 decimal places.

    Args:
        matrix : A list of lists containing integers/floats.
        div : The number to divide all elements by.

    Raises:
        TypeError: If matrix is not a list of lists of int/float
        TypeError: If rows in the matrix are not the same size
        TypeError: If div is not an integer or float
        ZeroDivisionError: If div is equal to 0
    
    Returns:
        list: A new matrix with all elements divided by div
        and rounded to 2 decimal places.
    """
    
    """Check if matrix is a list of lists of integers/floats"""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """Ensure all rows have the same size"""
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """Check if div is a number"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    """Check if div is zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    """Perform the division and round to 2 decimal places"""
    return [[round(el / div, 2) for el in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
