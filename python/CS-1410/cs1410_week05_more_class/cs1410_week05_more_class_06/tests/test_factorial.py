# # python -m unittest discover -vbs tests

import unittest

from factorial import *

import random


class Test_Factorial(unittest.TestCase):

    def test_01(self):
        values          = [ 0, 1, 2, 4, 8, 16, 32 ]
        correct_answers = [ 1, 1, 2, 24, 40320, 20922789888000, 263130836933693530167218012160000000 ]
        for i in range(len(values)):
            correct_answer = correct_answers[i]
            your_answer = factorial(values[i])
            self.assertEqual(correct_answer, your_answer)

        return
