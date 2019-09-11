#!/usr/bin/python3
def uppercase(str):
    i = 0
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            j = ord(str[i])
            j -= 32
        else:
            j = ord(str[i])

        print("{}".format(chr(j)), end='')
    print()
