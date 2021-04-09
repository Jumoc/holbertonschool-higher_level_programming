#!/usr/bin/python3
"""hbtn header module"""
import urllib.request, urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail = {'email': sys.argv[2]}
    # encode the data in the standard
    data = urllib.parse.urlencode(mail).encode('ascii')
    # pass the encoded data to the request object
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
