# Exercise 6
## Objective: using the function combine(word1, word2) from ex5.py, create a function counter(word) that will return the number of characters in the portmanteau
from ex05 import combine

def counter(word):
    return len(word)

portmanteau = combine("code", "NIH")
print counter(portmanteau)
