#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    num_element = len(my_list)

    if idx < 0:
        return my_list
    if idx >= num_element:
        return my_list

    my_list[idx] = element
    return my_list
