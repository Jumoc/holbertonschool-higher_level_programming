#!/usr/bin/python3
"""hbtn status module"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}\n\t- content: {}".format(
            type(content), content
        ))
