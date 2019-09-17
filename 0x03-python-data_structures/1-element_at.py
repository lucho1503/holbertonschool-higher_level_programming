#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if i > idx:
            return None
        elif idx < 0:
            return None
        else:
            if idx == i:
                return my_list[i]
