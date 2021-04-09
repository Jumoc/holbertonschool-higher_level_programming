#!/usr/bin/python3
"""hbtn status module"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    request = requests.post(url, data={'q': letter})
    try:
        r_dict = request.json()
        if r_dict.get('name') is None:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
