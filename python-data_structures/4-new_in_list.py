#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_copy = my_list.copy()

    if idx < 0 or idx >= len(new_copy):
        return (my_list)

    else:
        new_copy[idx] = element
        return (new_copy)
