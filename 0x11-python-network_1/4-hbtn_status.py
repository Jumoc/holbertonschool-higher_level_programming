#!/usr/bin/python3
"""hbtn status module"""
import requests


if __name__ == "__main__":
    request = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(
        type(request.text), request.text
    ))
