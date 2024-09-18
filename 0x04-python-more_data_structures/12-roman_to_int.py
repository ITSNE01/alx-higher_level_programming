#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    for i, char in enumerate(roman_string):
        temp = roman_values[char]
        try:
            if temp < roman_values[roman_string[i + 1]]:
                temp = temp * -1
        except IndexError:
            pass
        total = total + temp
    return total
