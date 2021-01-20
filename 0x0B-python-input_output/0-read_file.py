#!/usr/bin/python3
"""Module description for read_file"""


def read_file(filename=""):
    """prints the contents of a given file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
