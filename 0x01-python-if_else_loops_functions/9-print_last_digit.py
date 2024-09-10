#!/usr/bin/python3

# Prints and return the last digit of a number

def print_last_digit(number):
    # Get last digit using absolute value & % 10
    last_digit = abs(number) % 10
    # Print the last digit
    print(f"{last_digit}", end="")
    # Return the last digit
    return last_digit
