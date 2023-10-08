#!/usr/bin/python3

def element_at(my_list, idx):
    num_elements = len(my_list)

    if idx < 0:
        return None
    if idx >= num_elements:
        return None
    else:
        return my_list[idx]
