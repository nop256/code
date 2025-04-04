# # python -m unittest discover -vbs tests

import unittest

from rectangle import *

class Test_RectangleConstructor(unittest.TestCase):

    def test_01(self):
        r = Rectangle(1,2,3,4)
        s = Rectangle(4,3,2,1)

        # Can't really test anything yet.  Just make sure it runs
        self.assertTrue(True, "Can't really test anything yet.  Just make sure it runs")

        return
