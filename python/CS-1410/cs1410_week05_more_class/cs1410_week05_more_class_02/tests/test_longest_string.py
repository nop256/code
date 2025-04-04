# # python -m unittest discover -vbs tests

import unittest

from longest_string import *

import random

g_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def random_string(min_length, max_length):
    length = random.randrange(min_length, max_length+1)
    max_start  = len(g_alphabet) - length
    start = random.randrange(0, max_start+1)
    return g_alphabet[start:start+length]

def random_list_of_string(min_length, max_length, list_size):
    strings = []
    longest = ""
    for i in range(list_size):
        s = random_string(min_length, max_length)
        if len(s) > len(longest):
            longest = s
        strings.append(s)

    return strings, longest


class Test_LongestString(unittest.TestCase):

    def test_01(self):
        for i in range(10):
            strings, correct_answer = random_list_of_string(1, 62, random.randrange(1, 100))
            your_answer = longest_string(strings)
            self.assertEqual(correct_answer, your_answer)

        return
