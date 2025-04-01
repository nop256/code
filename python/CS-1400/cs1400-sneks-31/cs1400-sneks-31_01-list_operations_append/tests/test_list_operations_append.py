import ast
import unittest

import asttest

reset = "Reset your program by copying the starter code into this directory."

class TestListOperationsAppend(asttest.ASTTest):

    def setUp(self):
        super().setUp("list_operations_append.py")

    def test_required_syntax(self):
        lists = self.find_all(ast.List)
        self.assertGreaterEqual(len(lists), 1, "Do not change the "
                "initialization of `zoo`. " + reset)
        self.assertEqual(len(lists), 1, "You have created a second list. That "
                "is not correct! Remember, you should append *individual* "
                "elements, not a second list!")
        self.assertEqual(len(lists[0].elts), 0, "You cannot add elements to "
                "the empty list literal. Use the `append` method instead.")

        assigns = self.find_all(ast.Assign)
        self.assertNotEqual(len(assigns), 0, "You should not remove the `zoo`"
                " variable. " + reset)
        self.assertIs(type(assigns[0].value), ast.List, "The `zoo` variable "
                "should be a list.")

        calls = self.find_function_calls("append")
        self.assertEqual(len(calls), 0, "You appear to have called `append` as"
                " a function instead of a method. Fix it and try again.")

        methods = self.find_method_calls("append")
        if len(methods) < 1:
            self.fail("You need to use the `append` method.")
        if len(methods) < 3:
            self.fail("You need to use the `append` method 3 times.")

        if any([len(method.args) != 1 for method in methods]):
            self.fail("You should append one animal at a time.")
        if any([not isinstance(method.args[0], ast.Str) for method in methods]):
            self.fail("You should only append animal names as strings to the "
                    "`zoo` list.")

        animals = [method.args[0].s for method in methods]
        if len(animals) < 3:
            self.fail("You need to append 3 new animals to the `zoo` "
                    "variable.")
        if len(set(animals)) < 3:
            self.fail("Add 3 different animals; you have added some animals "
                    "more than once.")

        calls = self.find_function_calls("print")
        self.assertEqual(len(calls), 1, "You should print one time.")
        self.assertEqual(len(calls[0].args), 1, "You should print one thing.")
        self.assertIs(type(calls[0].args[0]), ast.Name, "You should print the "
                "zoo variable.")
        self.assertEqual(calls[0].args[0].id, "zoo", "You should print the zoo"
                " variable.")

if __name__ == "__main__":
    unittest.main()
