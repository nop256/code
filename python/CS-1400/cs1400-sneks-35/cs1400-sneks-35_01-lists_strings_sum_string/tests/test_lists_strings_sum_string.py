import ast
import unittest

import asttest

class TestListsStringsSumString(asttest.ASTTest):

    def setUp(self):
        super().setUp("lists_strings_sum_string.py")

    def test_required_syntax(self):
        self.assertIn("44,34,27,43,22,25", self.file, "Do not remove or change"
                " the original string literal that contains the numbers.")
        embed = "Do not embed the answer directly in the program. You should" \
                "calculate it with the for loop."
        for num in self.find_all(ast.Num):
            self.assertNotEqual(int(num.n), 195, embed)
        for str_ in self.find_all(ast.Str):
            self.assertNotEqual(str_.s, "195", embed)

        self.assertNotEqual(len(self.find_all(ast.For)), 0, "Do not remove the"
                " for loop.")
        self.assertNotEqual(len(self.find_function_calls("int")), 0, "Do not "
                "remove the int function call. You'll need to convert the "
                "numbers from a string to an int to properly add them.")
        self.assertNotEqual(len(self.find_function_calls("print")), 0, "Do not"
                " remove the print function call.")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything.")
        self.assertEqual(len(self.printed_lines), 1, "You should only print "
                "the final result.")
        self.assertNotEqual(self.printed_lines[0], 25, "You are printing the "
                "wrong final result. Perhaps you are printing the last element"
                " instead of the sum of all the elements?")
        self.assertEqual(self.printed_lines[0], 195, "You are printing the "
                "wrong final result.")


if __name__ == "__main__":
    unittest.main()
