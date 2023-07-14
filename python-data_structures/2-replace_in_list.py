#!/usr/bin/python3
# A function that replaces an element of a list at a specific position (like in C)

def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
