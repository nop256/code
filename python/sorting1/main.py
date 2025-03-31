import random
from bubblesort import bubble
from shakersort import shaker
from countingsort import counting
from quicksort import quicksortR
from quicksort_modified import quicksortRM
from mergesort2 import mergesort

def makerandom(list_length:int):
    numbers = []
    for i in range(list_length):
        numbers.append(random.randrange(0,list_length))
        #print(numbers) # check if random
    return numbers

def main():
    random_list = makerandom(20)
    print(f"\nOriginal List:")
    print(random_list)
    
    print(f"\nQuicksort:")
    quicksorted_list = random_list[:] #copying list
    quicksortR(quicksorted_list, 0, len(quicksorted_list) - 1,0)
    print(quicksorted_list)
    
    print(f"\nQuicksort Modified:")
    quicksorted_modified_list = random_list[:] #copying list
    quicksortRM(quicksorted_modified_list, 0, len(quicksorted_modified_list) - 1,0)
    print(quicksorted_modified_list)
    
    print(f"\nMergesort:")
    merged_sorted_list = random_list[:] # copying list
    mergesort(merged_sorted_list,0)
    print(merged_sorted_list)
    print(f"\n")
    
    print(f"\nCountingsort:")
    counted_list = random_list[:] #copying list
    counting(counted_list,0)
    print(counted_list)
    
main()