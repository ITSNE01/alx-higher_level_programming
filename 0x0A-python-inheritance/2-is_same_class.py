#!/usr/bin/python3
'''Module for is_same_class
'''


def is_same_class(obj, a_class):
    """ Returns True if obj is exactly an instance of a_class
    """
    return type(obj) == a_class
