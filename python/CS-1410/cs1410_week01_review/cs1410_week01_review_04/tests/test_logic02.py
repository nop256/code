# # python -m unittest discover -vbs tests

import unittest

from wsuminout import *

class Test_suminout(unittest.TestCase):

    def test_01(self):
        values = [ 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192 ]
        correct_answer = 16383 - 32 - 2048
        ans = suminout(values, 32, 2048)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))

    def test_02(self):
        values = [ 1 for i in range(1200) ]
        correct_answer = 0
        ans = suminout(values, 1, 2)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))

    def test_03(self):
        values = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]
        correct_answer = -64
        ans = suminout(values, 1, 10)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))

    def test_04(self):
        values = range(5, 501, 5)
        correct_answer = sum(range(5, 501, 5)) - 450 - 300
        ans = suminout(values, 450, 300)
        self.assertEqual(ans, correct_answer,
                         'You returned: %s. You should have returned %s. Check your logic and try again.' % (str(ans), str(correct_answer)))
