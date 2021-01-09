#!/usr/bin/python3
"""This is the module description for
    text indentation"""


def text_indentation(text):
    """Function that prints of a given size
    Args:
        first_name: first name
        last_name: last name
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    characters = (".", "?", ":")
    string = ""
    for ch in text:
        string += ch
        if ch in characters:
            print(string.strip())
            print()
            string = ""