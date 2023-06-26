#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for i in range(0, list_length):
        try:
            int_div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            int_div = 0
        except ZeroDivisionError:
            print("division by 0")
            int_div = 0
        except IndexError:
            print("out of range")
            int_div = 0
        finally:
            my_list.append(int_div)
    return (my_list)
