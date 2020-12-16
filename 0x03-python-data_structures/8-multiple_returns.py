#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        n_tuple = (len(sentence), None)
    else:
        n_tuple = (len(sentence), sentence[0])
    return n_tuple
