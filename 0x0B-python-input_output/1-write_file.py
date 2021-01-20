#!/usr/bin/python3
"""Module description for write_file"""


def write_file(filename="", text=""):
    """writes text to a given file"""
    with open(filename, "w",encoding="utf-8") as file:
        return file.write(text)
