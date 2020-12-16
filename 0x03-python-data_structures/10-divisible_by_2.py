#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_list = []
    [n_list.append(True if n % 2 == 0 else False) for n in my_list]
    return n_list
