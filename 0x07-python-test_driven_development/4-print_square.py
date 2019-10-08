#!/usr/bin/python3
def print_square(size):
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif size < 0 and type(size) is float:
        raise TypeError('size must be an integer')
    else:
        for i in range(size):
            print("{}".format('#' * size))
