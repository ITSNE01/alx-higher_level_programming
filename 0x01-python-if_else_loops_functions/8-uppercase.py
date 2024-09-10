#!/usr/bin/python3

# Print a string in uppercase followed by a new line
def uppercase(str):

    # Iterate over each char in the string
    for c in str:

        # Check if the char is lowercase w/ ASCII value
        if ord(c) >= 97 and ord(c) <= 122:

            # Convert lower to uppercase by - 32 from ASCII
            c = chr(ord(c) - 32)

        # Print the character without a newline
        print('{}'.format(c), end="")

    # Print a newline after the string is fully printed
    print()
