#!/usr/bin/python3

import json


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        my_list = []
        if list_objs is None:
            my_list = []
        else:
            for obj in list_objs:
                my_list.append(cls.to_dictionary(obj))
        strr = cls.to_json_string(my_list)
        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(strr)

    @staticmethod
    def from_json_string(json_string):
        my_list = []
        if json_string is None:
            return my_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if __name__ == "Square":
            dogo = cls(width=19, height=92)
        else:
            dogo = cls(92, 19)
        dogo.update(**dictionary)
        return dogo
