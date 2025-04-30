from random import randrange
def makerandom(size:int):
    numbers = []
    for i in range(size):
        numbers.append(randrange(0,size))
        print(numbers)
    return numbers
