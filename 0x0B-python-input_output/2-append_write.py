#!/usr/bin/python3
"""Module description for append_file"""


def append_write(filename="", text=""):
    """appends text to a given file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
