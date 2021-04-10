#!/usr/bin/python3
"""hbtn status module"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]
    request = requests.get('https://api.github.com/user', auth=(user, token))
    print(request.json().get('id'))
