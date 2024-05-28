#!/usr/bin/python3
"""A function that writes a string to a text file and returns the number of characters written."""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
        file.close()
    return
