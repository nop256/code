

def bubblesortwhile(A):
    changed = True
    while changed:
        changed = False
        for i in range(0-len(A)-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1], A[i]
                changed = True

def bubblesortbiggest(numbers):
    n = len(numbers)
    for i in range(n):
        for k in range (n-i-1):
            if numbers[k] > numbers[k+1]:
                numbers[k],numbers[k+1] = numbers[k+1], numbers[k]
        print(f"Pass:{i} {numbers}")

A = [9,2,7,3,12,2,1,0]
print(bubblesortwhile(A))
