#!/usr/bin/python3
"""a  script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    resp = {
        'type': type(response.read()),
        'content': response.read(),
        'utf8 content': response.read().decode('utf-8')
            }
print("Body response:")
for k, v in resp.items():
    print(f"\t- {k}: {v}")
