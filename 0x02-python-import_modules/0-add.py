#!/usr/bin/python3

if __name__ == "__main__":
    """
    It prints the sum of two numbers (a and b).
    """
    # Importing the 'add' function from the module 'add_0'
    from add_0 import add
    a = 1
    b = 2
    # Print the sum of x and y using the 'add' function
    print("{} + {} = {}".format(a, b, add(a, b)))
