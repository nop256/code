# # python -m unittest discover -vbs tests

import unittest

from scombostring import *


class TestHelloName(unittest.TestCase):

    def test_01(self):
        a = "Hello"
        b = "hi"
        correct_answer = "hiHellohi"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_02(self):
        a = "hi"
        b = "Hello"
        correct_answer = "hiHellohi"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_03(self):
        a = "aaa"
        b = "b"
        correct_answer = "baaab"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_04(self):
        a = "b"
        b = "aaa"
        correct_answer = "baaab"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_05(self):
        a = "aaa"
        b = ""
        correct_answer = "aaa"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_06(self):
        a = ""
        b = "bb"
        correct_answer = "bb"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_07(self):
        a = "aaa"
        b = "1234"
        correct_answer = "aaa1234aaa"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_08(self):
        a = "aaa"
        b = "bb"
        correct_answer = "bbaaabb"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_09(self):
        a = "a"
        b = "bb"
        correct_answer = "abba"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_10(self):
        a = "bb"
        b = "a"
        correct_answer = "abba"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))

    def test_11(self):
        a = "xyz"
        b = "ab"
        correct_answer = "abxyzab"
        ans = combo_string(a, b)
        self.assertEqual(ans, correct_answer, "You returned: {0}. You should have returned {1} when given {2} and {3} as your parameters.".format(ans, correct_answer, a, b))
