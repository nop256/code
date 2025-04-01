# # python -m unittest discover -vbs tests

import unittest

from vfourthchar import *

import random, os

def random_name():
    s = ""
    for i in range(8):
        c = chr(random.randint(ord('a'), ord('z')))
        s += c
    return s + ".txt"

def random_line():
    s = ""
    nchar = random.randint(1,10)
    for i in range(nchar):
        c = chr(random.randint(ord('a'), ord('z')))
        s += c
    return s

def random_lines():
    lines = []
    for i in range(20):
        line = random_line()
        lines.append(line)
    return lines

def random_text(filename):
    s = ""
    f = open(filename, "w")
    for i in range(20):
        line = random_line()
        f.write(line + "\n")
        s += line
    f.close()
    return s

def read_file(filename):
    s = ""
    f = open(filename, "r")
    for line in f:
        s += line
    f.close()
    return s

class Test_fourthchar(unittest.TestCase):

    def test_01(self):
        for i in range(10):
            filename = random_name()
            lines = random_lines()
            fourthchar(filename, lines)
            correct_answer = ""
            for line in lines:
                if len(line) > 3:
                    correct_answer += line[3]
                else:
                    correct_answer += "x"
            correct_answer += "\n"
            ans = read_file(filename)

            os.unlink(filename)
            msg = "fourthchar(%s, %s) stored %s." % (filename, str(lines), ans)
            msg = msg + "  It should have stored %s." % (correct_answer)
            msg = msg + "  Check your logic and try again."
            same = (ans == correct_answer)
            self.assertTrue(same, msg)
