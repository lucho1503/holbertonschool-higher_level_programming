#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) != 0:
        dic = sorted(a_dictionary.keys())
        for key in dic:
            print("{}: {}".format(key, a_dictionary[key]))
