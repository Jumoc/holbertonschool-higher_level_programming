#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = []
    result = 0
    for element in my_list:
        if not get_uniq(temp, element):
            result += element
            temp.append(element)
    return result


def get_uniq(mlist, n):
    for element in mlist:
        if element is n:
            return True
    return False
