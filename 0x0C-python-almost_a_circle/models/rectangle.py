#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be => 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be => 0')
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        i = 0
        has = self.y * '\n'
        while (i < self.height):
            has += (" " * self.x)
            has += ("#" * self. width) + '\n'
            i = i + 1
        print(has, end="")

    def __str__(self):
        id_dog = "({}) ".format(self.id)
        dogo_x_y = "{}/{}".format(self.x, self.y)
        dogo_w_h = " - {}/{}".format(self.width, self.height)
        return "[Rectangle] " + id_dog + dogo_x_y + dogo_w_h

    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            ret_args = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, ret_args[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
        """
        arg = len(args)
        if arg >= 1:
            self.id = args[0]
        if arg >= 2:
            self.__width = args[1]
        if arg >= 3:
            self.__height = args[2]
        if arg >= 4:
            self.__x = args[3]
        if arg >= 5:
            self.__y = args[4]
        """

    def to_dictionary(self):
        dicc = ['id', 'width', 'height', 'x', 'y']
        v = {}
        for k in dicc:
            v[k] = getattr(self, k)
        return v
