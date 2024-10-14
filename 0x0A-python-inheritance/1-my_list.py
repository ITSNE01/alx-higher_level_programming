#!/usr/bin/python3
'''Module for MyList class
'''


class MyList(list):
    ''' inherits from list() '''
    def print_sorted(self):
        """ method that prints the sorted list """
        print(sorted(self))
