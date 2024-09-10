#!/usr/bin/python3

# Prints a string in uppercase followed by a new line
def uppercase(str):
    result = ""
    # Single loop to iterate over each char in the string
    for c in str:
        # Check if the char is lowercase using ASCII
        if ord(c) >= 97 and ord(c) <= 122:
            # Convert lower to upper by - 32 from ASCII
            result += chr(ord(c) - 32)
        else:
            # Append the char as it is if it's not lowercase
            result += c
    # Print the entire result string followed by a newline
    print(f"{result}")
