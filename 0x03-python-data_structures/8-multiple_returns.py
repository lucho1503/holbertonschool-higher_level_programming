#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        my_tu = (0, None)
    else:
        my_tu = (len(sentence), sentence[0])
    return my_tu
