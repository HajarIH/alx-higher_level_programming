#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable"""
import sys
import urllib.request

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    req = response.headers.get('X-Request-Id')
print(req)
