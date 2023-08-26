#!/usr/bin/python3
def print_last_digit(number):
    NLD = abs(number) % 10
    print("{}".format(NLD), end="")
    return (NLD)
