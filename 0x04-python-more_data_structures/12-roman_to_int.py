#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i, char in enumerate(roman_string):
        temp = roman_values[char]
        if i + 1 < len(roman_string) and temp < roman_values[roman_string[i + 1]]:
            temp = -temp
        total += temp

    return total
