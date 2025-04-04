# # python -m unittest discover -vbs tests

import unittest

from xrandRangeParam2 import *

class Test_randRangeParam2(unittest.TestCase):

    def test_01(self):
        param1 = 5
        param2 = 15
        return_values = [ 0 for i in range(param1, param2 + 1) ]
        errors = 0
        for i in range((param2 - param1) * 15):
            ans = randRangeParam2(param1, param2)
            self.assertTrue(ans >= param1 and ans <= param2,
                            "Return value was outside of the desired range %d to %d.  You gave %d." % (param1, param2, ans))

            if ans >= param1 and ans <= param2:
                return_values[ans-param1] += 1

        for i in range(len(return_values)):
            self.assertTrue(return_values[i] > 0, "No values of %d were returned." % (param1 + i, ))

        return
