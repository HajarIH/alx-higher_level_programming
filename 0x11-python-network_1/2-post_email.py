#!/usr/bin/python3
"""script that takes in a URL and an email,
sends a POST request to the passed URL"""
import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')
with urllib.request.urlopen(url, data=data) as response:
    print("Your email is:", email)
