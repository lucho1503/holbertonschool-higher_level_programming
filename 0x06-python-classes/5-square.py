#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        i = 0
        has = "#"
        if (self.__size == 0):
            print()

        while (i < self.__size):
            print(has * self.__size)
            i = i + 1
