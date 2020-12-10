#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    i = 1
    while i < len(sys.argv):
        print("{:d}: {}".format(i, sys.argv[i]))
        i += 1