#!/usr/bin/python3
'''append_write'''


def append_write(filename="", text=""):
    """append filename with UTF-8"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
