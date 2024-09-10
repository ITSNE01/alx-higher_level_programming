#!/usr/bin/python3

# Loop through numbers from 0 to 99

for number in range(0, 100):

    # Check if it is the last number (99)
    if number == 99:
        # Print the last number followed by a new line
        print("{:02d}".format(number))
    else:
        # Print number w/ 2 digits, followed by ', ' w/out a new line
        print("{:02d}, ".format(number), end="")
