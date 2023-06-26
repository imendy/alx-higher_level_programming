#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        int_div = a / b
    except (TypeError, ZeroDivisionError):
        int_div = None
    finally:
        print("Inside result: {}".format(int_div))
    return (int_div)
