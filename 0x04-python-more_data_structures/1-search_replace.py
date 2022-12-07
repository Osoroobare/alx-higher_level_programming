#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element with another in a new list
    ...
    Parameters
    ----------
    my_list : list
        original list of elements
    search : integer
        The element to be replaced
    replace : integer
        The new element which has been inserted
    Return:
        a new list containing the new element
    """

    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
