# # python -m unittest discover -vbs tests

import unittest

from least_key import *

import random

g_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def random_string(min_length, max_length):
    length = random.randrange(min_length, max_length+1)
    max_start  = len(g_alphabet) - length
    start = random.randrange(0, max_start+1)
    return g_alphabet[start:start+length]

def random_dictionary_of_string_to_number(min_length, max_length, dictionary_size):
    dictionary = {}
    least = None
    for i in range(dictionary_size):
        key = random_string(min_length, max_length)
        value = random.randrange(1, 1000)
        if least is None or key < least:
            least = key
        dictionary[key] = value

    return dictionary, least


class Test_LeastKey(unittest.TestCase):

    def test_01(self):
        for i in range(10):
            strings, correct_answer = random_dictionary_of_string_to_number(1, 62, random.randrange(1, 100))
            your_answer = least_key(strings)
            self.assertEqual(correct_answer, your_answer)

        return
