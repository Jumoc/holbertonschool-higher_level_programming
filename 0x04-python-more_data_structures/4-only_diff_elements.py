#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for element in set_1:
        if not get_uniq(set_2, element):
            new_set.append(element)
    for element in set_2:
        if not get_uniq(set_1, element):
            new_set.append(element)
    return set(new_set)


def get_uniq(mlist, n):
    for element in mlist:
        if element is n:
            return True
    return False
