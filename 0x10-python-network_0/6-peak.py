#!/usr/bin/python3
"""Module peak"""

def find_peak(list_of_integers):
    """Finds the peak in a list of integers"""

    if len(list_of_integers) == 0:
        return None

    avg = sum(list_of_integers) / len(list_of_integers)

    for n in list_of_integers:
        if (n >= avg):
            return n
