#!/usr/bin/python3
"""
This is the "Rectangle" module.
This module provides a simple Rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes width and height, and
    methods area, perimeter, print, str, repr, and deletion message"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Prints the rectangle using the `#` character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a str repr of rectangle that can recreate an instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of rectangle. If width/height is 0, returns 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __del__(self):
        """Prints a message when the rectangle is deleted."""
        print("Bye rectangle...")
