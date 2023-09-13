#!/usr/bin/python3
"""Defines a string-to-JSON function"""
impory json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
