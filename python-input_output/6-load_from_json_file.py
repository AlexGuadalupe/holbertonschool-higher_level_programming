#!/usr/bin/python3
"""A function that creates an Object from a JSON file."""


def load_from_json_file(filename):
    """A function that creates an Object from a JSON file."""
    import json
    with open(filename, 'r') as file:
        """ 'r' es para leer el archivo"""
        return json.load(file)
