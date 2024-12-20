#!/usr/bin/python3
'''save_to_json_file'''


import json


def save_to_json_file(my_obj, filename):
    """Writes my_obj into text file"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
