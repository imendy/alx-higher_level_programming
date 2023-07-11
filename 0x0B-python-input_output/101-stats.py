#!/usr/bin/python3
"""Module to compute metrics based on input"""

import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

def compute_metrics():
    """Reads input from stdin, computes metrics, and prints statistics"""

    total_size = 0
    status_count = {code: 0 for code in status_codes}

    try:
        for i, line in enumerate(sys.stdin, 1):
            try:
                ip_address, _, _, status_code, file_size = line.split(' ')[0], line.split(' ')[-2], line.split(' ')[-1].strip()
                total_size += int(file_size)
                if status_code in status_count:
                    status_count[status_code] += 1

                if i % 10 == 0:
                    print("Total file size:", total_size)
                    for code in sorted(status_count.keys()):
                        if status_count[code] > 0:
                            print(code + ':', status_count[code])
                    print('')

            except (ValueError, IndexError):
                pass

    except KeyboardInterrupt:
        pass

    print("Total file size:", total_size)
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print(code + ':', status_count[code])


if __name__ == "__main__":
    compute_metrics()
