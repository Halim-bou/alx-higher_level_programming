#!/usr/bin/python3
"""
creat a Student class
"""


class Student:
    """function for the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        attrs_check = {}
        for attr in attrs:
            if hasattr(self, attr):
                attrs_check[attr] = getattr(self, attr)
        return attrs_check

    def reload_from_json(self, json):
        """replace all attributes of the class in instance"""
        for key, value in json.items():
            setattr(self, key, value)
