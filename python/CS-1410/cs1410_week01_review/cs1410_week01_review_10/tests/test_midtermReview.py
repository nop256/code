# # python -m unittest discover -vbs tests

import unittest

from qbiggest02 import *

class Test_biggest02(unittest.TestCase):

    def test_01(self):
        problems = [ (2, 3, 6),
                     (-2, 3, 1),
                     (-2, -3, 6),
                     (2, -3, -1), ]

        for i in range(len(problems)):
            x, y, correct_answer = problems[i]
            ans = biggest02(x, y)
            msg = "biggest02(%s, %s) returned %s." % (str(x), str(y), str(ans))
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (ans == correct_answer)
            self.assertTrue(same, msg)
