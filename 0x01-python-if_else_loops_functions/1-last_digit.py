#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
grater_five = "and is greater than 5"
zero = "and is 0"
less_six = "and is less than 6 and not 0"
print("Last digit of", end=" ")
if (number % 10 > 5):
    print("{} is {} {}".format(number, number % 10, grater_five))
