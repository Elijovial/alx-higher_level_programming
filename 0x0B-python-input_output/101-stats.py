#!/usr/bin/python3
import sys
"""Status codes"""


codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
status_codes = {code: 0 for code in codes}

total_size = 0
line_count = 0


def print_stats():
    """Prints the statistics of the input"""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


try:
    for line in sys.stdin:
        line_count += 1
        tokens = line.split()
        try:
            size = int(tokens[-1])
            status = tokens[-2]
            total_size += size
            if status in status_codes:
                status_codes[status] += 1
        except Exception:
            pass
        if line_count % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
