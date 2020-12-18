#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if type(roman_string) is not str:
        return result
    numbers = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
    for index in range(0, len(roman_string)):
        number = numbers.get(roman_string[index])
        if index != (len(roman_string) - 1) and numbers.get(roman_string[index + 1]) > number:
            result -= number
        else:
            result += number
    return result
