#!/usr/bin/python3
'''Student Creation Method'''


class Student:
    """Student representation"""

    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of student"""
        return self.__dict__
