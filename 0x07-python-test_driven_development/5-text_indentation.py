#!/usr/bin/python3
"""Module to handle text indentation."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    
    skip_space = False

    for char in text:
        if char in ['.', '?', ':']:
            result += char + "\n\n"
            skip_space = True
        else:
            if skip_space and char == " ":
                continue

            result += char
            skip_space = False

    print("\n".join([line.strip() for line in result.splitlines()]))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
