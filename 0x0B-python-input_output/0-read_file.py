#!/usr/bin/python3
"""Module description for read_file"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
