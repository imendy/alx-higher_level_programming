#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elem = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elem += 1
        except IndexError:
            break
    print("")
    return (elem)
