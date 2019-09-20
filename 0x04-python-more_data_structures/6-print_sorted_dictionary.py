#!/usr/bin/python3
def print_sorted_dictionary(dictionary):
    for keys in sorted(dictionary.keys()):
        print("{:s} : {}".format(keys, dictionary[keys]))
