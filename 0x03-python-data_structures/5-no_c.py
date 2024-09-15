#!/usr/bin/python3
def no_c(my_string):
    # Create a new str by filtering out 'c' & 'C'
    new_string = ''.join(char for char in my_string if char != 'c' and char != 'C')
    return new_string
