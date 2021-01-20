#!/usr/bin/python3
"""This is a module definition"""


class MyList(list):
    """MyList class that inherits from class list"""
    def print_sorted(self):
        """Prints the list sorted in decending order"""
        print(sorted(self))
