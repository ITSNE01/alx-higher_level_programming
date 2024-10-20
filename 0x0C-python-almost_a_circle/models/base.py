#!/usr/bin/python3
'''Base Class Module'''
import json
import csv
import os.path


class Base:
    """ Class Base representation """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
