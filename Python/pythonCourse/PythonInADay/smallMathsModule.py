## Making your own module

## import the function randint from the random module
from random import randint

def multiplyBy5(x):
    return 5 * x

def add5(x):
    return x + 5

## get a random integer between 0 and 10
def randomAdd(x):
    y = randint(0,10)
    return x + y
