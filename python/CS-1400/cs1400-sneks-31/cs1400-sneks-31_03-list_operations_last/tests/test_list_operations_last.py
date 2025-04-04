import ast
import sys
import unittest

import asttest

reset = "Reset your program by replacing it with the file in the starter folder."

class TestListOperationsLast(asttest.ASTTest):

    def setUp(self):
        super().setUp("list_operations_last.py")

    def test_required_syntax(self):
        lists = self.find_all(ast.List)
        self.assertNotEqual(len(lists), 0, "You should not remove the list "
                "literal value. " + reset)
        self.assertEqual(len(lists), 1, "You should not add new list literals. "
                + reset)
        self.assertGreaterEqual(len(lists[0].elts), 3, "You should not remove "
                "elements from the list literal. " + reset)
        if any(not isinstance(e, ast.Str) for e in lists[0].elts):
            self.fail("You should not change any elements of the list literal. "
                    + reset)
        if tuple([e.s for e in lists[0].elts]) != ("Not me", "Nor me", "Print me!"):
            self.fail("You should not change the given list. " + reset)

        subscripts = self.find_all(ast.Subscript)
        self.assertNotEqual(len(subscripts), 0, "You will need to subscript "
                "the list.")
        self.assertEqual(len(subscripts), 1, "You should only subscript the "
                "list once.")
        self.assertIsInstance(subscripts[0].slice, correct_subscript_type(), "You should be "
                "using list indexing to access the last element.")
        self.assertIsInstance(subscripts[0].value, ast.List, "You should only "
                "be indexing the list literal.")

        if sys.version_info >= (3, 9):
            if isinstance(subscripts[0].slice, ast.Constant):
                self.assertNotEqual(subscripts[0].slice.value, 2, "You are accessing"
                        " the third element, which happens to be the last element this"
                        " time. But what if you were given a list of a different "
                        "length? I recommend using a more convenient way to access "
                        "the last element of a sequence, regardless of its length.")
                self.fail("You should be accessing the last element of the list.")
            self.assertIsInstance(subscripts[0].slice, ast.UnaryOp, "You "
                    "should be accessing the last element of the list.")
            self.assertIsInstance(subscripts[0].slice.operand, ast.Constant, "You"
                    " should be accessing the last element of the list.")
            self.assertEqual(subscripts[0].slice.operand.value, 1, "You should "
                    "be accessing the last element of the list.")
        else:
            if isinstance(subscripts[0].slice.value, ast.Num):
                self.assertNotEqual(subscripts[0].slice.value.n, 2, "You are accessing"
                        " the third element, which happens to be the last element this"
                        " time. But what if you were given a list of a different "
                        "length? I recommend using a more convenient way to access "
                        "the last element of a sequence, regardless of its length.")
                self.fail("You should be accessing the last element of the list.")
            self.assertIsInstance(subscripts[0].slice.value, ast.UnaryOp, "You "
                    "should be accessing the last element of the list.")
            self.assertIsInstance(subscripts[0].slice.value.operand, ast.Num, "You"
                    " should be accessing the last element of the list.")
            self.assertEqual(subscripts[0].slice.value.operand.n, 1, "You should "
                    "be accessing the last element of the list.")

        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print one "
                "thing.")
        self.assertEqual(self.printed_lines[0], "Print me!", "You are not "
                "printing the right thing.")

def correct_subscript_type():
    if sys.version_info >= (3, 9):
        return ast.UnaryOp
    return ast.Index

if __name__ == "__main__":
    unittest.main()
