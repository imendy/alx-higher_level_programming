#!/usr/bin/python3
""" Module to print status code """
import sys


class StatusCodeAnalyzer:
    """ Class to generate instances with dictionary and size"""
    def __init__(self):
        """ Init method """
        self.status_dict = {}
        self.size = 0

    def init_status_dict(self):
        """ Initialize dictionary """
        self.status_dict['200'] = 0
        self.status_dict['301'] = 0
        self.status_dict['400'] = 0
        self.status_dict['401'] = 0
        self.status_dict['403'] = 0
        self.status_dict['404'] = 0
        self.status_dict['405'] = 0
        self.status_dict['500'] = 0

    def add_status_code(self, status):
        """ Add repeated number to the status code """
        if status in self.status_dict:
            self.status_dict[status] += 1

    def print_info(self, sig=0, frame=0):
        """ Print status code """
        print("File size: {:d}".format(self.size))
        for key in sorted(self.status_dict.keys()):
            if self.status_dict[key] != 0:
                print("{}: {:d}".format(key, self.status_dict[key]))


if __name__ == "__main__":
    analyzer = StatusCodeAnalyzer()
    analyzer.init_status_dict()
    nlines = 0

    try:
        for line in sys.stdin:
            if nlines % 10 == 0 and nlines != 0:
                analyzer.print_info()

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                analyzer.add_status_code(list_line[-2])
                analyzer.size += int(list_line[-1].strip("\n"))
            except:
                pass
            nlines += 1
    except KeyboardInterrupt:
        analyzer.print_info()
        raise
    analyzer.print_info()
