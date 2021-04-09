#!/usr/bin/python3
"""hbtn status module"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
            type(content), content,
            content.decode('utf-8')
        ))
