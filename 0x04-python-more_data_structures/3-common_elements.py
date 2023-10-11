#!/usr/bin/python3

def common_elements(set_1, set_2):
    commonEle = set()
    for elements in set_1:
        if elements in set_2:
            commonEle.add(elements)
    return commonEle
