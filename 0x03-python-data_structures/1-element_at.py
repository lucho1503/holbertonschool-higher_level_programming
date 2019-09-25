#!/usr/bin/python3
def element_at(my_list, idx):
    for i, ent in enumerate(my_list):
        if idx < 0:
            return None
        if idx == i:
            return ent
    return None
