from cisc108 import assert_equal

def add_positives(num1,num2):
    sum = num1+num2
    if sum > 0:
        return sum
    else:
        return 0

assert_equal(add_positives(2,4),6)
assert_equal(add_positives(-1,-3),0)









'''
29.4) Stay Positive

Create a function named `add_positives` that consumes two numbers and returns
their sum. However, this function should only add positive numbers. Therefore,
if either number is less than zero, you should instead return `0`. Make sure to
unit test your function.
'''
