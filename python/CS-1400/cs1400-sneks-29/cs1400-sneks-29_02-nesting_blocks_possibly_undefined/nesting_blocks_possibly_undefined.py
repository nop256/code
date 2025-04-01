from cisc108 import assert_equal
def calculate_income(salary):
    tax = .90
    if salary > 5000:
        return salary * tax
    else:
        return salary
assert_equal(calculate_income(1000), 1000)
assert_equal(calculate_income(10000), 9000.0)




'''
Instructions
29.2: Possibly Undefined

The function `calculate_income` in the given program is broken. Fix the function
so that it will correctly decrease the passed-in salary by 10% but only if the
salary is greater than $5,000 per year. Otherwise, it should return the salary
un-adjusted.
'''
