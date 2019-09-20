#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    else:
        new = []
        for i in matrix:
            my_list = list(map((lambda x: x ** 2), i))
            new.append(my_list)
        return (new)
