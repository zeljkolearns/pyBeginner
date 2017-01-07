# Exercise 8
## Objective: create a function timer(num); when run it should count down from "num" seconds, while printing each iteration number
from time import sleep


def timer(num):
    for element in range(num, 0, -1):
        print element
        sleep(1)

timer(10)
