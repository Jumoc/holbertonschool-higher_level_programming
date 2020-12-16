#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or (len(my_list) - 1) < idx:
        return my_list
    nlist = my_list[:]
    nlist[idx] = element
    return nlist
