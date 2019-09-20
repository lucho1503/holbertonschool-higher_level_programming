#!/usr/bin/python3
def mul(num):
    return num * 2

def multiply_by_2(a_dictionary):
    new = {}
    for i in a_dictionary:
      new[i] = (a_dictionary[i] * 2)
    return new
