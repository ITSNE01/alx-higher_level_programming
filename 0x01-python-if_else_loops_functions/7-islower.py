#!/usr/bin/python3

# Function to check if a character is lowercase
def islower(c):
    # ord() to get ASCII and check range of lowercase
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
