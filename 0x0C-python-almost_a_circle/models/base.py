#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """define private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a json string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = []
                for obj in list_objs:
                    the_dic = obj.to_dictionary()
                    list_dictionaries.append(the_dic)
                f.write(Base.to_json_string(list_dictionaries))
