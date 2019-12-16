#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if not i:
            print()
        for index, val in enumerate(i):
            print("{:d}".format(val), end='')
            if index != (len(i) - 1):
                print(" ", end='')
            else:
                print()
