# # python -m unittest discover -vbs tests

import unittest

from zpartlist2 import *

class Test_partlist2(unittest.TestCase):

    def test_01(self):
        parameters = [ ([ 11, 13, 17, 19, 23, 29 ], 1, 2),
                       ([ 11, 13, 17, 19, 23, 29 ], 2, 2),
                       ([ 11, 13, 17, 19, 23, 29 ], 3, 2),
                       ([ 11, 13, 17, 19, 23, 29 ], 0, 3),
                       ([ 11, 13, 17, 19, 23, 29 ], 1, 3),
                       ([ 11, 13, 17, 19, 23, 29 ], 2, 3),
                       ([ 11, 13, 17, 19, 23, 29 ], 3, 3),
                       ([ 11, 13, 17, 19, 23, 29 ], 4, 3), ]
        correct_answers = [ [ 13, 19, 29 ],
                            [ 17, 23 ],
                            [ 19, 29 ],
                            [ 11, 19 ],
                            [ 13, 23 ],
                            [ 17, 29 ],
                            [ 19 ],
                            [ 23 ], ]

        for i in range(len(parameters)):
            correct_answer = correct_answers[i]
            lst, a, b = parameters[i]
            ans = partlist2(lst, a, b)

            msg = "partlist2(%s, %s, %s) returned %s." % (str(lst), str(a), str(b), str(ans))
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (ans == correct_answer)
            self.assertTrue(same, msg)

        return
