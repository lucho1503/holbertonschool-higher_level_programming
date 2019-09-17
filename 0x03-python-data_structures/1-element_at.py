#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx == i:
            return my_list[i]
        if idx < 0:
            return None
        if i > idx:
            return None
