#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = 2
    for key in a_dictionary:
        a_dictionary[key] = a_dictionary.get(key) * mul
    return a_dictionary