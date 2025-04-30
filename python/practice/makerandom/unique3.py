from random import shuffle
def makeuniquerandom(size:int):
    """generates a randomized number list conisting entirely of unique numbers at O(n) work"""
    numbers=list(range(1,size+1)) #generates a sequence of numbers from 1 to size (inclusive)
    print(numbers)      #prints the unrandomized list for testing purposes
    shuffle(numbers)    #shuffles the list of numbers to appear randomly generated
    return numbers
