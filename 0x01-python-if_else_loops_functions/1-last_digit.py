#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
NLD = abs(number) % 10
if NLD > 5:
    print(f"Last digit of {number} is {NLD} and is greater than 5")
elif NLD == 0:
    print(f"Last digit of {number} is {NLD} and is 0")
else:
    print(f"Last digit of {number} is {NLD} and is less than 6 and not 0")
