# # python -m unittest discover -vbs tests

import unittest

from battery import *

class Test_BatteryConstructor(unittest.TestCase):

    def test_01(self):
        c = Battery(3080.)
        d = Battery(17.)

        # Can't really test anything yet.  Just make sure it runs
        self.assertTrue(True, "Can't really test anything yet.  Just make sure it runs")

        return
