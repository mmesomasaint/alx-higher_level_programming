#!/usr/bin/python3
def search_replace(my_list, search, replace):
    idx = []
    for i, value in enumerate(my_list):
        if value == search:
            idx.append(i)
    for index in idx:
        my_list[index] = replace
    return my_list
