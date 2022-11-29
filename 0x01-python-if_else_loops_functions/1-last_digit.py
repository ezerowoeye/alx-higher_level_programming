#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = int(str(number)[-1])
if number < 0:
    LastDigit = LastDigit * -1
else:
    LastDigit = LastDigit * 1
first = "Last digit of "
last = " and is less than 6 and not 0"
if(lastDigit > 5):
    print(first + "{} is {} and is greater than 5".format(number, lastDigit))
elif(lastDigit == 0):
    print(first + "{} is {} and is 0".format(number, lastDigit))
else:
    print(first + "{} is {}".format(number, lastDigit) + last)
