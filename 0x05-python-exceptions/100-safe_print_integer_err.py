#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception: {}".format(ve), file=stderr)
        return False
    except TypeError as te:
        print("Exception: {}".format(te), file=stderr)
        return False
    else:
        return True
