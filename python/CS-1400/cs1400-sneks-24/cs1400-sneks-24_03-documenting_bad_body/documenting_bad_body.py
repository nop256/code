def force_palindrome(a_word):
    '''
    This function creates a palindrome from a phrase by adding
    the reverse of the phrase to its end.

    Args:
        a_word (str): Any string of text
    Returns:
        str: a string twice as long with the reverse'''

    return a_word + a_word[::-1]

print(force_palindrome('AB'))
