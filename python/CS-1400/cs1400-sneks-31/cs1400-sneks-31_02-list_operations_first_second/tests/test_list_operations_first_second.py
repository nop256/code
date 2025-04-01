import ast
import sys
import unittest

import asttest

reset = "Reset your program by replacing it with the file from the starter " \
        "folder."

class TestListOperationsFirstSecond(asttest.ASTTest):

    def setUp(self):
        super().setUp("list_operations_first_second.py")

    def test_required_syntax(self):
        assigns = self.find_all(ast.Assign)
        self.assertNotEqual(len(assigns), 0, "You should not remove the "
                "`temperatures` variable assignment statement. " + reset)
        self.assertNotEqual(len(assigns[0].targets), 0, "You should not change"
                " the `temperatures` variable assignment statement. " + reset)
        self.assertEqual(assigns[0].targets[0].id, "temperatures", "You "
                "should not change the `temperatures` variable assignment "
                "statement. " + reset)
        self.assertIsInstance(assigns[0].value, ast.List, "You should not "
                "change the `temperatures` variable assignment statement. " +
                reset)
        temperatures = []
        for elt in assigns[0].value.elts:
            self.assertIsInstance(elt, ast.Num, "You should not change the "
                    "`temperatures` variable assignment statement. " + reset)
            temperatures.append(elt.n)
        self.assertEqual(tuple(temperatures), (50, 60, 55, 35, 50, 65), "You "
                "should not change the given list. " + reset)

        lists = self.find_all(ast.List)
        self.assertEqual(len(lists), 1, "You should not create any other "
                "lists. That is not correct!")

        subscripts = self.find_all(ast.Subscript)
        self.assertGreaterEqual(len(subscripts), 2, "You will need to "
                "subscript the list twice.")

        if not all(subscript_is_correct_type(s) for s in subscripts):
            self.fail("You should be using list indexing to access the first "
                    "and second elements.")

        if not all((isinstance(s.value, ast.Name)) and (s.value.id == "temperatures") for s in subscripts):
            self.fail("You should only be indexing the `temperatures` "
                    "variable.")
        if tuple(sorted(get_subscript_value(s) for s in subscripts)) == (1, 2):
            self.fail("You need to index the first and second element. "
                    "Remember, Python thinks that `0` is the first element.")
        if tuple(sorted(get_subscript_value(s) for s in subscripts)) != (0, 1):
            self.fail("You need to index the first and second element.")

        self.exec_solution()
        if 50 != self.printed_lines[0] and 60 != self.printed_lines[1]:
            self.fail("You are not printing the right thing.")

def subscript_is_correct_type(s):
    if sys.version_info >= (3, 9):
        return isinstance(s.slice, ast.Constant)
    return isinstance(s.slice, ast.Index)

def get_subscript_value(s):
    if sys.version_info >= (3, 9):
        return s.slice.value
    return s.slice.value.n

if __name__ == "__main__":
    unittest.main()
