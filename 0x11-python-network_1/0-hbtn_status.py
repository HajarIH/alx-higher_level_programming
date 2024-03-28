#!/usr/bin/python3
"""a  script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read().decode('utf-8')
    resp = {
        'type': type(content),
        'content': content,
        'utf8 content': content
        }
    print("Body response:")
    for k, v in resp.items():
        print(f"\t- {k}: {v}")
