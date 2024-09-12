#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print the addition of all arguments."""

    sum_int = 0
    for i in range(len(sys.argv) - 1):
        sum_int += int(sys.argv[i + 1])
    print("{}".format(sum_int))
