#!/usr/bin/python3
"""
Base class
"""
import json
import csv


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
            return []
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
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                dict_list = Base.from_json_string(f.read())
                return [cls.create(**dic) for dic in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    list_names = ["id", "width", "height", "x", "y"]
                else:
                    list_name = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, list_names=list_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    list_names = ["id", "width", "height", "x", "y"]
                else:
                    list_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, list_names=list_names)
                new_dicts = []
                for d in list_dicts:
                    new_dict = {}
                    for k, v in d.items():
                        new_dict[k] = int(v)
                    new_dicts.append(new_dict)
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
