#!/usr/bin/python3

# Iterate over the 1st digit (0-9)
for i in range(0, 10):
    # Iterate over the 2nd digit, ensuring 2nd > 1st
    for j in range(i + 1, 10):
        # Check if it's the last combo (89) to print
        if i == 8 and j == 9:
            print("89")
        else:
            # Print the combo followed by ", " w/out newline
            print('{}{}, '.format(i, j), end="")
