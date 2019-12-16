#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding="utf-8") as f:
        if nb_lines <= 0:
            msg = f.read()
            print(msg, end="")
        else:
            n = 0
            for line in f:
                print(line, end="")
                n = n + 1
                if n == nb_lines:
                    break
