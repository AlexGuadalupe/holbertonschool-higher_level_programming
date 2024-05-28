#!/usr/bin/python3
"""A function that writes a string to a text file and returns the number of characters written."""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout."""

    with open(filename) as file:
        print(file.read(), end="")
