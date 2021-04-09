#!/usr/bin/python3
"""hbtn status module"""
import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    if int(request.status_code) >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
