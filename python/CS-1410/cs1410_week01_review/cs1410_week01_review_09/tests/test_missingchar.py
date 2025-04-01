# # python -m unittest discover -vbs tests

import unittest

from rmissingchar import *


class TestMissingChar(unittest.TestCase):

    def test_1(self):
        correct_answer = 'ktten'
        ans = missing_char('kitten', 1)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))

    def test_2(self):
        correct_answer = 'itten'
        ans = missing_char('kitten', 0)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))

    def test_3(self):
        correct_answer = 'kittn'
        ans = missing_char('kitten', 4)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))

    def test_4(self):
        correct_answer = 'i'
        ans = missing_char('Hi', 0)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))

    def test_5(self):
        correct_answer = 'H'
        ans = missing_char('Hi', 1)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))

    def test_6(self):
        correct_answer = 'ode'
        ans = missing_char('code', 0)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))

    def test_7(self):
        correct_answer = 'cde'
        ans = missing_char('code', 1)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))

    def test_8(self):
        correct_answer = 'coe'
        ans = missing_char('code', 2)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))

    def test_9(self):
        correct_answer = 'cod'
        ans = missing_char('code', 3)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))

    def test_10(self):
        correct_answer = 'chocolat'
        ans = missing_char('chocolate', 8)
        self.assertEqual(correct_answer, ans, "You returned: {0}, when you should have returned '{1}'.".format(ans, correct_answer))


# missing_char('kitten', 1) -> 'ktten'	'ktten'	OK
# missing_char('kitten', 0) -> 'itten'	'itten'	OK
# missing_char('kitten', 4) -> 'kittn'	'kittn'	OK
# missing_char('Hi', 0) -> 'i'	'i'	OK
# missing_char('Hi', 1) -> 'H'	'H'	OK
# missing_char('code', 0) -> 'ode'	'ode'	OK
# missing_char('code', 1) -> 'cde'	'cde'	OK
# missing_char('code', 2) -> 'coe'	'coe'	OK
# missing_char('code', 3) -> 'cod'	'cod'	OK
# missing_char('chocolate', 8) -> 'chocolat'	'chocolat'	OK
