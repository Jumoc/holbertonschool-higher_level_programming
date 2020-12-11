#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, __stderr__
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    operators = "+-*/"
    if operators.find(argv[2]) == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = 0
    index = 0
    if argv[2] == operators[0]:
        result = add(int(argv[1]), int(argv[3]))
        index = 0
    elif argv[2] == operators[1]:
        result = sub(int(argv[1]), int(argv[3]))
        index = 1
    elif argv[2] == operators[2]:
        result = mul(int(argv[1]), int(argv[3]))
        index = 2
    elif argv[2] == operators[3]:
        result = div(int(argv[1]), int(argv[3]))
        index = 3
    print("{} {} {} = {}".format(argv[1], operators[index], argv[3], result))
