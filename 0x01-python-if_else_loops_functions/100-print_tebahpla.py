#!/usr/bin/python3
# Loop through ASCII values of letters from 'z' to 'a'
for i in range(ord('z'), ord('a') - 1, -1):
    # If ASCII value is even, set diff to 0 (lowercase)
    if i % 2 == 0:
        diff = 0
    else:
        # If ASCII is odd, set diff to 32
        # (convert to uppercase by - 32)
        diff = 32
    # Print char after adjusting w/ diff, w/out a new line
    print('{}'.format(chr(i - diff)), end='')
