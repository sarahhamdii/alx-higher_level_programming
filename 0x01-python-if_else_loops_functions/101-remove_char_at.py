#!/usr/bin/python3
def remove_char_at(str, n):
    value = ""
    for i in range(len(str)):
        if i != n:
            value = value + str[i]
    return (value)
