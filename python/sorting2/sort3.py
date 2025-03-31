import random, sys, math
from bubblesort import bubble
from shakersort import shaker
from countingsort import counting
from quicksort import quicksort
from quicksort import modquick
from mergesort2 import mergesort

def makerandom(list_length:int):
    numbers = []
    for i in range(list_length):
        numbers.append(random.randrange(0,list_length))
        #print(numbers) # check if random
    return numbers

def mostlysorted(size):
    C = makerandom(size)
    C.sort()
    #print(C)
    C[0],C[len(C)-1] = C[len(C)-1],C[0]
    #print(C)
    return C

def main(branch):
    sys.setrecursionlimit(10000)
    algorithms= [bubble,shaker,counting,mergesort, quicksort, modquick]
    
    print(f"{'':<4} {'Bubble':<9} {'Shaker':<9} {'Counting':<9} {'Merge':<9} {'Quick':<9} {'MQuick':<10}")
    for s in range(3,12+1):
        size = 2 ** s
        row = f"{s:02}   "
        #print(s, end=" ")

        for sort in algorithms:
            A = makerandom(size)
            if branch == 1:
                A = makerandom(size)
            elif branch == 2:
                B = mostlysorted(size) #B = copy of list AB.sort()
            count = [0]
            sort(A, count)
            try:
                row += f"{math.log(count[0], 2):<10.2f}"
            except ValueError:
                row += f"{'error!':<10}"
            #if A != B:
                #row += f"{'error!':<10}"
        print(row)
        
main(1
print()
main(2)

