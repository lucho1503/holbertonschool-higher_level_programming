#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """inizializate method"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id_dog = "({}) ".format(self.id)
        x_y_dog = "{}/{} - ".format(self.x, self.y)
        size_dog = "{}".format(self.size)
        return "[Square] " + id_dog + x_y_dog + size_dog

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            arg_ret = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, arg_ret[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        dicc = ['id', 'size', 'x', 'y']
        v = {}
        for k in dicc:
            v[k] = getattr(self, k)
        return v
