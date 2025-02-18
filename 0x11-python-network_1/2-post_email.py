#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse as parse
import urllib.request as request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("ascii")
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        res = response.read().decode("utf-8")
        print(res)
