#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    [new_list.append(element) if element != search
        else new_list.append(replace) for element in my_list]
    return new_list
