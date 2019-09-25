#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    new = my_list.copy()
    for i, ent in enumerate(new):
        if i == idx:
            new[i] = element
    if idx <= i:
        return new
    else:
        return my_list
