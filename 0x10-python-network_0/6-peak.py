#!/usr/bin/python3
"""Module peak"""


def find_peak(list_of_integers):
    """Finds the peak in a list of integers"""
    if len(list_of_integers) != 0:
        list_of_integers.sort()
        return list_of_integers[-1]
