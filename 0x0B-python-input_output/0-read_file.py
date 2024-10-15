#!/usr/bin/python3
'''read_file'''


def read_file(filename=""):
    """Reads filename with UTF-8"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
