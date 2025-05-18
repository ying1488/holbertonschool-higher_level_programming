#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        res = a_dictionary[key] * 2
        new_dict[key] = res
    return new_dict
