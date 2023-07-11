#!/usr/bin/python3
'''
Function that inserts a line of text to a file,
after each line containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    '''Function to insert a line in specific string'''
    z = ''
    with open(filename) as file:
        for the_txt in file:
            z += the_txt
            if search_string in the_txt:
                z += new_string
    with open(filename, 'w') as f:
        f.write(z)
