#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list
    ...
    Parameters
    ----------
    my_list : list
        elements list
    Return:
        the result of the operation
    """

    result = 0
    for x in set(my_list):
        result += x
    return (result)
