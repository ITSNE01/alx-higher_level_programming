#!/usr/bin/python3
'''Module for Rectangle class
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Subclass that inherits from Rectangle """

    def __init__(self, size):
        """ Constructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ String representation of square """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
