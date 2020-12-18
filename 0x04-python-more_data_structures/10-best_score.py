#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
            return None
    greaterValue = -1000
    greaterKey = ""
    for key in a_dictionary.keys():
        if a_dictionary.get(key) > greaterValue:
            greaterValue = a_dictionary.get(key)
            greaterKey = key
    return greaterKey
