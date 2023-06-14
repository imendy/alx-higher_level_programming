#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    sum = 0
    for num in my_list:
        if num not in unique_list:
            unique_list.append(num)
            sum += num
    return sum
