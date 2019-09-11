#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i < j and not(i == 8 and j == 9):
            print("{}{}".format((i), (j)), end=", ")
print(89)
