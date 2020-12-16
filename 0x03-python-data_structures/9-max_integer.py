#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    big = -1000
    for n in my_list:
        if n > big:
            big = n
    return big
