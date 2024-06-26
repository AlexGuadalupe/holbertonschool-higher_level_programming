#!/usr/bin/python3
"""a class Student"""


class Student:
    """a class Student that defines a student
    (9-student.py)"""

    def __init__(self, first_name, last_name, age):
        """initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary"""
        if attrs is None:
            return self.__dict__

        Newdict = {}
        for a in attrs:
            try:
                Newdict[a] = self.__dict__[a]
            except KeyError:
                pass
        return Newdict
