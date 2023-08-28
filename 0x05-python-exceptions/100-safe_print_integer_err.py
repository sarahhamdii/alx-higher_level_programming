#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        int_value = int(value)
        print("{:d}".format(int_value))
        return True
    except (TypeError, ValueError) as mas:
        print("Exception: {}".format(mas), file=sys.stderr)
        return False
