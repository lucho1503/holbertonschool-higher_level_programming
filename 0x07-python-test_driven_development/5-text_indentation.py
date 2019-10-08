#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    signs = ".:?"
    for i in text:
        print("{}".format(i), end='')
        if i in signs:
            print()
            print()
