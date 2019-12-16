#!/usr/bin/python3
class MyInt(int):
    def __init__(self, size):
        self.size = size

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
