#!/usr/bin/python3
"""a Python script that takes in a URL and an email
address, sends a POST request to the passed URL"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    load = {'email': email}
    response = requests.post(url, data=load)
    print("Your email is:", email)
