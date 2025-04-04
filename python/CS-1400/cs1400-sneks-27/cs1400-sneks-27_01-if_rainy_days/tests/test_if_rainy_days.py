import ast
import unittest

import asttest

m1 = "It will probably rain."
m2 = "It might not rain."

class TestIfRainyDays(asttest.ASTTest):

    def setUp(self):
        super().setUp("if_rainy_days.py")

    def test_required_syntax(self):
        self.assertNotIn("%", self.file, "You should not use a % in your code."
                " How do you represent a number like 50% in Python?")
        ifs = self.find_all(ast.If)
        self.assertGreaterEqual(len(ifs), 1, "You will need an if statement.")
        self.assertEqual(len(ifs), 1, "You only need one <code>if</code> statement.")

        str_values = [s.s for s in self.find_all(ast.Str)]
        self.assertIn(m1, str_values, 'Make sure you have the message "{}" in '
                'your code.'.format(m1))
        self.assertIn(m2, str_values, 'Make sure you have the message "{}" in '
                'your code.'.format(m2))

        num_values = [n.n for n in self.find_all(ast.Num)]
        if .5 not in num_values and 50 not in num_values:
            self.fail("You will need to represent the number 50% as a float "
                    "literal value. How should you represent 50% as a decimal "
                    "number?")

        prints = self.find_function_calls("print")
        self.assertGreaterEqual(len(prints), 1, "You are printing the wrong "
                "number of times.")

    def test_correct_result(self):
        self.exec_solution()
        if m1 not in self.printed_lines and m2 not in self.printed_lines:
            self.fail("You are not printing the right output.")

if __name__ == "__main__":
    unittest.main()
