# # python -m unittest discover -vbs tests

import unittest

from ylettersuptochar import *

class Test_letters_up_to_char(unittest.TestCase):

    def test_01(self):
        param1 = "heresmylongstring"
        param2 = "i"
        correct_answer = param1[:param1.find(param2)]
        ans = letters_up_to_char(param1, param2)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))

    def test_02(self):
        param1 = "supercalifragilisticexpialidoshus"
        param2 = "x"
        correct_answer = param1[:param1.find(param2)]
        ans = letters_up_to_char(param1, param2)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))

    def test_03(self):
        param1 = "bob"
        param2 = "o"
        correct_answer = param1[:param1.find(param2)]
        ans = letters_up_to_char(param1, param2)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))

    def test_04(self):
        param1 = "sometimesithrowup"
        param2 = "w"
        correct_answer = param1[:param1.find(param2)]
        ans = letters_up_to_char(param1, param2)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))

    def test_05(self):
        param1 = "thisisasadsong"
        param2 = "d"
        correct_answer = param1[:param1.find(param2)]
        ans = letters_up_to_char(param1, param2)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))

    def test_06(self):
        param1 = "abcdefghijklmnop"
        param2 = "h"
        correct_answer = param1[:param1.find(param2)]
        ans = letters_up_to_char(param1, param2)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))

    def test_07(self):
        param1 = "abcdefghijklmnop"
        param2 = "a"
        correct_answer = param1[:param1.find(param2)]
        ans = letters_up_to_char(param1, param2)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))
