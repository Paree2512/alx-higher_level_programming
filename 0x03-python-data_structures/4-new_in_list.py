#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy_ls = my_list.copy()
    num_element = len(my_list)
    if idx < 0:
        return copy_ls
    if idx >= num_element:
        return copy_ls

    copy_ls[idx] = element
    return copy_ls
