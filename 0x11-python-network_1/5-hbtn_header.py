#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the
URL and displays the value of the variable X-Request-Id"""
import requests
import sys

url = sys.argv[1]

