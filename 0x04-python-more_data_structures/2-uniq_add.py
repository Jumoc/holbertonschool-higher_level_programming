#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = []
    result = 0
    for element in my_list:
        if get_uniq(temp, element) == False:
            result += element
            temp.append(element)
    return result

def get_uniq(mlist, n):
    for element in mlist:
        if element == n:
            return True
    return False