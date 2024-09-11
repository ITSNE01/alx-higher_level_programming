#!/usr/bin/python3
def magic_calculation(a, b, c):
    # First condition: if a < b
    if a < b:
        return c  # If true, return c
    # Second condition: if c > b
    if c > b:
        return a + b  # If true, return the sum
    # Default case
    return (a * b) - c
