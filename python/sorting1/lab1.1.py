import random

def makerandom(list_length:int):
    numbers = []
    for i in range(list_length):
        numbers.append(random.randrange(0,list_length))
        #print(numbers) # check if random
    return numbers

def bubble(numbers):
    n = len(numbers)
    flag = True
    while flag: # outer loop, iterate until False  
        flag = False
        for i in range(0, n-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                flag = True

def shaker(numbers):
    n = len(numbers)
    flag = True
    while flag:
        flag = False
        for i in range(n-2,-1,-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                flag = True
            print(numbers)
    

def counting(numbers):
    n = len(numbers)
    F=[]
    # or :: F= [0]*len(numbers)
    for i in range(n):
        F.append(0)
    for i in A:
        F[i]+=1
    k=0
    for i in range(n):
        count=F[i]
        value=i
        for j in range(count):
            A[k]=value
            k+=1

def main():
    random_list = makerandom(20)
    print(random_list)
    shaker(random_list)
    print(random_list)
    
    
    
main()