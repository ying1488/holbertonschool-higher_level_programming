#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for x in my_list:
        res.append(x % 2 == 0)
    return res
