#!/usr/bin/python3
"""hbtn status module"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    request = requests.post(url, data={'q': letter})
    r_dict = eval(request.text)
    if r_dict is None:
        print("Not a valid JSON")
    elif r_dict.get('name') is None:
        print("No result")
    elif "{" in request.text and "}" in request.text:
        print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
