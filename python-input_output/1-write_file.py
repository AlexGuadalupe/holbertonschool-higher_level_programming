#!/usr/bin/python3
"""A function that writes a string to a text file and returns the number
of characters written."""


def write_file(filename="", text=""):
    """A function that writes a string to a text file and returns the number
    of characters written."""
    with open(filename) as file:
        return file.write(text)
