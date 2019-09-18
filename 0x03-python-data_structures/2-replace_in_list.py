#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i, ent in enumerate(my_list):
        if idx < 0:
            return my_list
        if idx == i:
            my_list[i] = element
    return my_list
