#!/usr/bin/python3
"""a  script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    content_utf = content.decode('utf-8')
    resp = {
        'type': type(content),
        'content': content,
        'utf8 content': content_utf
        }
    print("Body response:")
    for k, v in resp.items():
        print(f"\t- {k}: {v}")
