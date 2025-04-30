from random import shuffle

def makeuniquerandom(size:int):
    numbers=list(range(size))
    shuffle(numbers)
    return numbers
