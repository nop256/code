import ast
import unittest

import asttest

class TestListsBookList(asttest.ASTTest):

    def setUp(self):
        super().setUp("lists_book_list.py")

    def test_list(self):
        declarations = len(self.find_all(ast.List)) + len(self.find_function_calls("list"))
        if declarations < 1:
            self.fail("You must create a list.")
        elif declarations > 1:
            self.fail("You should only have one list.")

        assigns = self.find_all(ast.Assign)
        if len(assigns) < 1:
            self.fail("You must use an assignment statement to create a "
                    "variable to hold your list.")
        elif len(assigns) > 1:
            self.fail("You should only have one assignment statement.")

        self.assertEqual(len(assigns[0].targets), 1, "You should assign to one"
                " variable.")
        variable = assigns[0].targets[0].id

        self.assertIs(type(assigns[0].value), ast.List, "You should assign "
                "your list to the variable.")
        list_elts = assigns[0].value.elts
        if len(list_elts) < 3:
            self.fail("You need at least 3 strings in your list variable.")
        if any([not isinstance(elt, ast.Str) for elt in list_elts]):
            self.fail("All of the elements in the list must be strings.")

        calls = self.find_function_calls("print")
        self.assertEqual(len(calls), 1, "You should print one time.")
        self.assertEqual(len(calls[0].args), 1, "You should print the list.")
        self.assertIs(type(calls[0].args[0]), ast.Name, "You should print the "
                "list.")
        self.assertEqual(calls[0].args[0].id, variable, "You should print the "
                "list.")

if __name__ == "__main__":
    unittest.main()
