#!/usr/bin/python3
""" takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=payload)
    try:
        res = response.json()
        if not res:
            print("No result")
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print("Not a valid JSON")
