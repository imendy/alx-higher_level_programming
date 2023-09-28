#!/usr/bin/python3
"""
Find Peak task 6
"""

def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    list_length = len(list_of_integers)
    if list_length == 1:
        return list_of_integers[0]
    elif list_length == 2:
        return max(list_of_integers)

    mid = int(list_length / 2)
    current_element = list_of_integers[mid]
    if current_element > list_of_integers[mid - 1] and current_element > list_of_integers[mid + 1]:
        return current_element
    elif current_element < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
