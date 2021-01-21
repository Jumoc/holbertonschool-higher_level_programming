#!/usr/bin/python3
"""Module description for add_item"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


file = "add_item.json"
try:
    open(file, "r", encoding="utf-8")
except:
    save_to_json_file(sys.argv[1:], file)
else:
    m_list = load_from_json_file(file)
    m_list += (sys.argv[1:])
    save_to_json_file(m_list, file)
