# # python -m unittest discover -vbs tests

import unittest

from tsum13 import *


class TestSum13(unittest.TestCase):

    def test_01(self):
        nums = [1, 2, 2, 1]
        correct_answer = 6
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_02(self):
        nums = [1, 1]
        correct_answer = 2
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_03(self):
        nums = [1, 2, 2, 1, 13]
        correct_answer = 6
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_04(self):
        nums = [1, 2, 13, 2, 1, 13]
        correct_answer = 4
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_05(self):
        nums = [13, 1, 2, 13, 2, 1, 13]
        correct_answer = 3
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_06(self):
        nums = []
        correct_answer = 0
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_07(self):
        nums = [13]
        correct_answer = 0
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_08(self):
        nums = [13, 13]
        correct_answer = 0
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_09(self):
        nums = [13, 0, 13]
        correct_answer = 0
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_10(self):
        nums = [13, 1, 13]
        correct_answer = 0
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_11(self):
        nums = [5, 7, 2]
        correct_answer = 14
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_12(self):
        nums = [5, 13, 2]
        correct_answer = 5
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_13(self):
        nums = [0]
        correct_answer = 0
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))

    def test_14(self):
        nums = [13, 0]
        correct_answer = 0
        ans = sum13(nums)
        self.assertEqual(ans, correct_answer, "You returned {0}. You should have returned {1}. Check your logic and try again.".format(ans, correct_answer))
