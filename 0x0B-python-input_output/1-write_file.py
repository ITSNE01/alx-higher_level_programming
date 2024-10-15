#!/usr/bin/python3
'''write_file'''


def write_file(filename="", text=""):
    """Read filename with UTF-8"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
