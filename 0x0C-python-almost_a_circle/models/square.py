#!/usr/bin/python3
"""
class Square that inherits a class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """inizializate method"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns [class] (id) x/y - size """
        id_dog = "({}) ".format(self.id)
        x_y_dog = "{}/{} - ".format(self.x, self.y)
        size_dog = "{}".format(self.size)
        return "[Square] " + id_dog + x_y_dog + size_dog

    @property
    def size(self):
        """ return the private instance """
        return self.width

    @size.setter
    def size(self, size):
        """ set the value of a property """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ assigns values to the attributes """
        if args is not None and len(args) is not 0:
            arg_ret = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, arg_get[i], args[i]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return the representation of a dictionary """
        dicc = ['id', 'size', 'x', 'y']
        v = {}
        for k in dicc:
            if key == 'size':
                v[k] = getattr(self, 'width')
            else:
                v[k] = getattr(self, k)
        return v
