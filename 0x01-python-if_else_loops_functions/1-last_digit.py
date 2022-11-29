#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = int(str(number)[-1])
if number < 0:
    LastDigit = LastDigit * -1
else:
    LastDigit = LastDigit * 1
if LastDigit > 5:
    print("Last digit of {} is {} and is greater than \
5".format(number, LastDigit))
elif LastDigit == 0:
    print("Last digit of {} is {} and is 0".format(number, LastDigit))
elif LastDigit < 6:
    print("Last digit of {} is {} and is less than \
6 and not 0".format(number, LastDigit))
