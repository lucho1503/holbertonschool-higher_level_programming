#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = sorted(a_dictionary.keys())
    for key in dic:
        print("{:s} : {}".format(key, a_dictionary[key]))
