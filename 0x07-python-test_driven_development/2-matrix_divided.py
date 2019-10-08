#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    lenght = len(matrix[0])
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            if type(matrix[i]) is not list:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            if len(matrix[i]) != lenght:
                raise TypeError('Each row of the matrix must have the same size')
            if type(matrix[i][j]) is not int and type(matrix[i][j]) != float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            n = round((matrix[i][j] / 3), 2)
            new_matrix[i].append(n)
    return new_matrix
