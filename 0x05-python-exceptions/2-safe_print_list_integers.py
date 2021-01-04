#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, j = -1, 0
    while i < x:
        i += 1
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            continue
        except IndexError:
            break
        else:
            j += 1
    print("")
    return j
