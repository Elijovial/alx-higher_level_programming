#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        numerator = sum(map(lambda x: x[0] * x[1], my_list))
        denominator = sum(map(lambda x: x[1], my_list))
        if denominator == 0:
            return 0
        else:
            return numerator / denominator
