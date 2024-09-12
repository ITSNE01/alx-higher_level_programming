#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of a and b"""

    # Import 'add' function from module 'add_0'
    from add_0 import add
    a = 1
    b = 2
    # Print sum of a and b using 'add' function
    print("{} + {} = {}".format(a, b, add(a, b)))
