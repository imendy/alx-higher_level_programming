#!/usr/bin/python3
"""creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """
        creates an Object from JSON file
    """
    with open(filename, 'r') as file:
        return json.loads(file.read())
