#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
         return fct(args[0], args[1])
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
        return None
