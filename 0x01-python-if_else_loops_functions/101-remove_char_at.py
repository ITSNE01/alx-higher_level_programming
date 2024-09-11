#!/usr/bin/python3
def remove_char_at(str, n):
    # Create a new string by concatenating all chars
    # except the one at index n
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str
