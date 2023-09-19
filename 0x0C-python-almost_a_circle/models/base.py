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

    @staticmethod
    def from_json_string(json_string):
        """return a list of json string representation json_sting"""
        if json_string is None or json_string == "":
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_dic = cls(1, 1)
        else:
            new_dic = cls(1)
        new_dic.update(**dictionary)
        return new_dic

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name) + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                dict_list = Base.from_json_string(f.read())
                return [cls.create(**d) for dic in dict_list]
        except IOError:
            return []
