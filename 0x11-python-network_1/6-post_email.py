#!/usr/bin/python3
"""hbtn status module"""
import requests
import sys


if __name__ == "__main__":
    request = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(request.text)
