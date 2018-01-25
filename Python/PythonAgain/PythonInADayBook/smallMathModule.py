''' --- Making my own module --- '''
 # import 'randint' function from 'random module'
from random import randint

def multiplyBy5(x):
    return 5 * x

def add5(x):
    return x + 5

def randomAdd(x):
    # recieves random int from 0 - 10
    y = randint(0, 10)
    return x + y
