from random import shuffle
def makeuniquerandom(size:int):
    numbers=list(range(1,size+1))
    print(numbers)
    shuffle(numbers)
    return numbers
