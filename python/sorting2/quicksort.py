#B = [4,2,5,7,3,0,6,5]

def quicksortR(A,low,high, mod):
    """
    A = (array of numbers)
    L = low index (0)
    H = high index(len(A)-1)
    """
    if high-low <= 0:
        return
    
    if mod:
        mid = (high + low) // 2
        A[low], [mid] = A[mid], [low]
    
    pvalue = A[low]
    lmgt= low + 1
    
    for i in range(low + 1, high + 1):
        if A[i] < pvalue:
            A[i],A[lmgt] = A[lmgt],A[i]
            lmgt+=1
            
    pivotindex = lmgt - 1
    A[low], A[pivotindex] = A[pivotindex], A[low]
    
    quicksortR(A, low, pivotindex-1, mod)
    quicksortR(A, pivotindex+1, high, mod)
    
def quicksort(A, mod=False):
    quicksortR(A, 0, len(A)-1, mod)
    
def modquick(A, mod=True):
    quicksortR(A, 0, len(A)-1, mod)
    
    
    
B = [4,2,5,7,3,0,6,5]
quicksort(B, False)
print(B)