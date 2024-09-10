#!/usr/bin/python3
# Loop through ASCII values of lowercase letters from 'a' to 'z'
for ascii_value in range(ord('a'), ord('z') + 1):
    # Skip the letters 'q' and 'e'
    if ascii_value != ord('q') and ascii_value != ord('e'):
        # Print char corresponding to ASCII value, w/out a new line
        print('{:c}'.format(ascii_value), end='')
