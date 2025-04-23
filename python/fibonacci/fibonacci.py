
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a + b
        a = b
        b = temp
    return a

def fibonacciR(n):
    if n==0 or n==1: return 1
    return fibonacciR(n-1)+fibonacciR(n-2)

def fibonacaciR2(n):
    return 1 if n==0 or n==1 else fibonacciR2(n-1)+fibonacciR2(n-2)
