#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for element1 in set_1:
        for element2 in set_2:
            if element1 == element2:
                common.append(element1)
    return set(common)
