#!/usr/bin/python3
import sys
def my_function(argv):
        if len(argv) == 1:
            print("{:d} argument.".format(len(argv) - 1))
        for i in range(1, len(argv)):
            if len(argv) == 2:
                print("{:d} argument:".format(len(argv) - 1))
                print("{:d}: {}".format(i, argv[
i]))
        if len(argv) > 2:
            print("{:d} arguments:".format(len(argv) - 1))
            for i in range(1, len(argv)):
                print("{:d}: {}".format(i, argv[i]))

my_function(sys.argv)
