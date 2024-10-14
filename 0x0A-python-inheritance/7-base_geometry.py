#!/usr/bin/python3
'''Module for BaseGeometry class
'''


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Computes area and raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
