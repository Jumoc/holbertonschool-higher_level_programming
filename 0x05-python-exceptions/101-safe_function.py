#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    value = None
    try:
        value = fct(args[0], args[1])
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
        return value
    else:
        return value
