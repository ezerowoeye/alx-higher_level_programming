#!/usr/bin/python3
import random                                                                                                                                                             
number = random.randint(-10000, 10000)
LastDigit = int(str(number)[-1])
if number < 0:
    LastDigit = LastDigit * -1
else:
    LastDigit = LastDigit * 1
if LastDigit > 5:
    print(f"Last digit of {number:d} is {LastDigit:d} and is greater than 5")
elif LastDigit == 0:
    print(f"Last digit of {number:d} is {LastDigit:d} and is 0")
elif LastDigit < 6: 
    print(f"Last digit of {number:d} is {LastDigit:d} and is less \
than 6 and not 0")