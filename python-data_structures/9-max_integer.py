#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_list.sort()
        largest = my_list[-1]
        return (largest)
    else:
        return (None)
