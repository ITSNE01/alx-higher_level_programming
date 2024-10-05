#!/usr/bin/python3
"""Module that provides the add_integer function."""

def add_integer(a, b=98):
    """
    Adds two int or floats, and returns their sum as int
    
    Args:
        a (int, float): First number to add.
        b (int, float): Second number to add, default is 98.
    
    Raises:
        TypeError: If either a or b is not an integer or float.
    
    Returns:
        int: The sum of a and b as an integer.
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    
    """Cast both numbers to int before performing addition"""
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
