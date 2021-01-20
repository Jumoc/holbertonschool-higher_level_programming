#!/usr/bin/python3
"""Module description for load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an object from a json"""
    with open(filename, encoding="utf-8") as file:
        m_json = json.loads(file.read())
    return m_json
