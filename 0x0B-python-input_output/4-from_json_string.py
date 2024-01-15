#!/usr/bin/python3
"""from json string to object"""


import json


def from_json_string(my_str):
    """ a function that returns a JSON string"""
    return json.loads(my_str)
