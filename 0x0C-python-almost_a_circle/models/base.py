#!/usr/bin/python3
"""
class Base - this class will be the base of all other classes in this project.
"""
import json


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ inizializate id and incremented __nb_onjects """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return the representation string of a JSON """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write the representation of string JSON in a file .json"""
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
        """ return the list of the representation of string JSON """
        my_list = []
        if json_string is None:
            return my_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return a instanse with all already set """
        if cls.__name__ == "Rectangle":
            dogo = cls(19, 92)
        else:
            dogo = cls(92)
        dogo.update(**dictionary)
        return dogo
