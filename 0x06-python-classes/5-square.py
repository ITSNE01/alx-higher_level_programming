#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        self.size = size  # Calls the setter for validation

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")  # Prints an empty line if size is 0
        else:
            for i in range(self.__size):
                print("#" * self.__size)
