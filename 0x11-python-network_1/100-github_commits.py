#!/usr/bin/python3
""" takes 2 arguments in order to solve this challenge
"""
import requests
from sys import argv


if __name__ == "__main__":
    count = 0
    url = (f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits")
    res = requests.get(url)

    for idx in res.json():
        if count < 10:
            print(f"{idx.get('sha')}: {idx.get('commit').get('author').get('name')}")
        count += 1
