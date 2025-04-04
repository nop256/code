from cisc108 import assert_equal

def is_odd(a_number):
    '''
    Consumes a number and determines if it is odd.

    Args:
        a_number (int or float): Any valid number
    Returns:
        bool: Whether or not the number was odd
    '''
    return a_number % 2 == 1
