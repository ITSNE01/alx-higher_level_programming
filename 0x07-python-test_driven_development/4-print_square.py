#!/usr/bin/python3
"""Module to print a square using the character #."""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size of the square's side.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    
    """Check if size is an integer"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    """Check if size is non-negative"""
    if size < 0:
        raise ValueError("size must be >= 0")
    
    """Print the square"""
    for _ in range(size):
        print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
