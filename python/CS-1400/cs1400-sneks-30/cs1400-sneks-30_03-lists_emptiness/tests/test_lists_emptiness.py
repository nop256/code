import ast
import unittest

import asttest

class TestListsEmptiness(asttest.ASTTest):

    def setUp(self):
        super().setUp("lists_emptiness.py")

    def test_required_syntax(self):
        self.assertNotEqual(len(self.file), 0, "Your program has nothing in "
                "it!")

        self.assertEqual(len(self.find_all(ast.Assign)), 0, "The question does"
                " not ask you to create any variables!")

        self.assertEqual(len(self.find_all(ast.List)), 1, "You should create "
                "one list.")

        prints = self.find_function_calls("print")
        self.assertEqual(len(prints), 1, "You should print one time.")
        self.assertEqual(len(prints[0].args), 1, "You should print one thing.")
        self.assertIs(type(prints[0].args[0]), ast.List, "You are printing the"
                " wrong thing. You should print an empty list literal.")
        self.assertEqual(len(prints[0].args[0].elts), 0, "You are printing the"
                " wrong thing. You should print an empty list literal.")

if __name__ == "__main__":
    unittest.main()
