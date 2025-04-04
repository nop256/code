# # python -m unittest discover -vbs tests

import unittest

from color import *

class Test_ColorConstructor(unittest.TestCase):

    def test_01(self):
        reds    = [ 0, 100, 200, 255 ]
        greens  = [ 0, 100, 200, 255 ]
        blues   = [ 0, 100, 200, 255 ]

        for red in reds:
            for green in greens:
                for blue in blues:
                    c = Color(red, green, blue)
                    # Can't really test anything yet.  Just make sure it runs
                    self.assertTrue(True, "Can't really test anything yet.  Just make sure it runs")

        return
