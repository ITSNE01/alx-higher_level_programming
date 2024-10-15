#!/usr/bin/python3
'''load_from_json_file'''


import json


def load_from_json_file(filename):
    """creates obj fron json file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
