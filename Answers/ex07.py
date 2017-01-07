# Exercise 7
## Objective: import the sleep function from the time package; have this script print "No sleep, no prob" every 2 seconds for 20 seconds
from time import sleep

i = 0

while i < 10:
    print "No sleep, no prob"
    sleep(2)
    i += 1
