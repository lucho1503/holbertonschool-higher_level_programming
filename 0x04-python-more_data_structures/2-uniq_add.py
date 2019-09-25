#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    if my_list is None:
        return suma
    else:
        mylist = list(set(my_list))
        for i in mylist:
            suma = suma + i
        return suma
