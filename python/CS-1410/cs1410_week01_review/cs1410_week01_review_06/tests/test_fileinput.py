# # python -m unittest discover -vbs tests

import unittest

from ufifthchar import *

import random, os

def random_name():
    s = ""
    for i in range(8):
        c = chr(random.randint(ord('a'), ord('z')))
        s += c
    return s + ".txt"

def random_line():
    s = ""
    nchar = random.randrange(1, 10)
    for i in range(nchar):
        c = chr(random.randint(ord('a'), ord('z')))
        s += c
    return s

def random_text(filename):
    s = ""
    f = open(filename, "w")
    for i in range(20):
        line = random_line()
        f.write(line + "\n")
        if len(line) > 4:
            s += line[4]
    f.close()
    return s

class Test_fifthchar(unittest.TestCase):

    def test_01(self):
        for i in range(10):
            filename = random_name()
            correct_answer = random_text(filename)
            ans = fifthchar(filename)
            os.unlink(filename)
            msg = "fifthchar(%s) returned %s." % (filename, ans)
            msg = msg + "  It should have returned %s." % (correct_answer)
            msg = msg + "  Check your logic and try again."
            same = (ans == correct_answer)
            self.assertTrue(same, msg)
