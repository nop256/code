from cisc108 import assert_equal

def rate_animal(animal):
    if animal == "dog":
        return 1
    elif animal == "cat":
        return 2
    elif animal == "capybara":
        return 3
    elif animal == "danger noodle":
        return 4 
    else:
        return -1

print(rate_animal("dog"))

assert_equal(rate_animal("dog"), 1)
assert_equal(rate_animal("cat"), 4)












'''
# 29.3) Animal Rater

Create a function named `rate_animal` that will rate the value of different
animals on a numeric scale (1-4, where 1 is best and 4 is worst). Your function
should consume a variable named `animal` that represents the type of animal as a
string, and return an integer from 1-4 for each of four respective inputs:
`"dog"`, `"cat"`, `"capybara"`, and `"danger noodle"`. Each animal should have
its own value. If the string given is not one of these animals, return `-1`.

Use your function to print out the rating for your favorite animal. You should
consider writing unit tests, but you are not required to do so.
'''

