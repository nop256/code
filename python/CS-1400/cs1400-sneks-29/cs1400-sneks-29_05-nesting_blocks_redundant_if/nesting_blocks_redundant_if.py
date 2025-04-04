from cisc108 import assert_equal


def am_i_on_fire(temperature):
    return temperature > 109


assert_equal(am_i_on_fire(100), False)
assert_equal(am_i_on_fire(110), True)









'''
29.5) Redundant If

The function in the given program uses an unnecessary `if/else` statement.
_Refactor_ the function (modify it without changing its behavior) so that it no
longer uses an `if/else` statement but produces the same result.
'''

