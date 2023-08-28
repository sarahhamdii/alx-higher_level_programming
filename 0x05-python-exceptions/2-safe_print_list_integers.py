#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            n = 0
            print("{:d}".format(my_list[i]), end="")
            n = n + 1
        except (ValueError, TypeError):
            continue
    print("")
    return (n)

