#!/usr/bin/python3
"""despues lo hago"""


from curses.textpad import rectangle
import json


class Base:
    """despues lo hago de nuevo"""
    __nb_objects = 0

    def __init__(self, id=None):

        """otro comentario"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """lo hago despues"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """lo hago despues"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(cls.to_json_string(
                        [element.to_dictionary() for element in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """lo hago despues"""
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """comentario"""
        if cls.__name__ == "Rectangle":
            dummy = cls(9, 8)
        if cls.__name__ == "Square":
            dummy = cls(9)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """read file in json format and return a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as myfile:
                to_read = myfile.read()
                lists_dic = cls.from_json_string(to_read)
                lists = []
                for k in lists_dic:
                    lists.append(cls.create(**k))
                return lists
        except Exception:
            return []
