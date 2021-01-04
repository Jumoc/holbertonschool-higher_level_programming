#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, j = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            i += 1
            continue
        else:
            j += 1
            i += 1
    print("")
    return j
