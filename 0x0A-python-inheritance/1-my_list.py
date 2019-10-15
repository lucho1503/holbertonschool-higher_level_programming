#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        milist = self.copy()
        milist.sort()
        print(milist)
