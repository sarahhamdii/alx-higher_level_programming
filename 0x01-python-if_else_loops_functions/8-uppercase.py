#!/usr/bin/python3
def uppercase(str):
    up = ""
    for i in str:
        if ord(i) >= 95 and ord(i) <= 122:
            up = up + chr(ord(i) - 32)
        else:
            up = up + i
    print("{}".format(up))
