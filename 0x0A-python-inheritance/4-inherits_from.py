#!/usr/bin/python3
'''Module for inherits_from method'''


def inherits_from(obj, a_class):
    """ Determines if obj is a true subclass of a_class """
    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    return False
