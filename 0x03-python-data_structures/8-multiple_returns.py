#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size != 0:
        b = sentence[0]
    else:
        b = None
    return (size, b)
