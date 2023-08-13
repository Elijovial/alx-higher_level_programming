#!/usr/bin/python3
def my_infinite(argument):
    if len(argument) == 1:
        print("0")
    else:
        result = 0
        for i in range(1, len(argument)):
            result += int(argument[i])
        total = result
        print(total)

if __name__ == "__main__":
    import sys
    my_infinite(sys.argv)
