#A = [4,2,5,7,3,0,6,5]

def modquicksortR(A,L,H, count):
    """
    L = low index (0)
    H = high index(0-1)
    """
    if H-L <= 0: # base case
        return
    
    mid = (L + H) // 2
    A[L], A[mid] = A[mid], A[L]
    
    pvalue = A[L]#PIvot value
    lmgt=L+1 #index for elements greater than pivot value
    #partitioning
    for i in range(L+1,H+1):
        if A[i] < pvalue:
            A[i],A[lmgt] = A[lmgt],A[i]
            lmgt+=1
            
    pivotindex= lmgt - 1
    A[L], A[pivotindex] = A[pivotindex], A[L]
    
    #recursively sorting L and R partitions
    modquicksortR(A, L, pivotindex-1)
    modquicksortR(A, pivotindex+1, H)