#!/usr/bin/python3
def weight_average(my_list=[]):
    div_0 = 0
    div_1 = 1
    milist = []
    for i, j in my_list:
        div_0 += i * j
        milist.append(j)
    if len(milist) > 0:
        div_1 = 0
    for num in milist:
        div_1 += num
    return div_0 / div_1
