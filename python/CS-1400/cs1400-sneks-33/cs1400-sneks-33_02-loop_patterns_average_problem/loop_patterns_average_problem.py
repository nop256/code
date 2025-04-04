from cisc108 import assert_equal
# 33.2) An Average Problem


numbers = [1,2,3,4,5]
sum = 0
def average(lst):
    for number in lst:
       average =  sum + number
    return float(average)


print(average([1,2,3,4,5]))



'''
for page in pages_count_list:
    sum_pages = sum_pages + page
'''

'''
Create a function named `average` that consumes a list of numbers
and returns their average (as a float) by combining the Sum
and Count patterns:

    average = sum / count

Unit test your function.'''
