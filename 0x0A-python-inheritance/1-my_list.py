#!/usr/bin/python3
"""MyList class inheriting from list class"""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """prints the sorted list."""

        copy_list = self.copy()
        copy_list.sort()
        print("{}".format(copy_list))
