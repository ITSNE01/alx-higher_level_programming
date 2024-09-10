#!/usr/bin/python3

# Prints numbers from 1 to 100 with Fizz, Buzz & FizzBuzz
def fizzbuzz():
    # Iterate through numbers from 1 to 100
    for i in range(1, 101):
        # Check if number is divisible by 3 & 5 (FizzBuzz)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # Check if the number is divisible by 3 (Fizz)
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # Check if the number is divisible by 5 (Buzz)
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # For all other numbers, print the number itself
        else:
            print(f"{i}", end=" ")
