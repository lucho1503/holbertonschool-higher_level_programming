#!/usr/bin/python3
"""
class Square that inherits a class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Rectancgle """

    def __init__(self, size, x=0, y=0, id=None):
        """inizializate method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns [class] (id) x/y - size """
        id_dog = "({}) ".format(self.id)
        x_y_dog = "{}/{} - ".format(self.x, self.y)
        size_dog = "{}/{}".format(self.width, self.height)
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
        """ assigns key/values to the attributes """
        if args is not None and len(args) is not 0:
            arg_ret = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if arg_ret == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, arg_ret[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return the representation of a dictionary """
        dicc = ['id', 'size', 'x', 'y']
        v = {}
        for k in dicc:
            v[k] = getattr(self, k)
        return v
