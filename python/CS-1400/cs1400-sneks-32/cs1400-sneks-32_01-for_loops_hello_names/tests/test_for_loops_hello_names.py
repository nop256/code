import ast
import unittest

import asttest

reset = "Check the starter code and try again."

class TestForLoopsHelloNames(asttest.ASTTest):

    def setUp(self):
        super().setUp("for_loops_hello_names.py")

    def test_required_syntax(self):
        fors = self.find_all(ast.For)
        self.assertNotEqual(len(fors), 0, "Do not remove the for loop. " +
                reset)
        self.assertEqual(len(fors), 1, "Do not add any additional for loops. "
                + reset)

        assigns = self.find_all(ast.Assign)
        self.assertEqual(len(assigns), 2, "Do not add or remove any assignment"
                " statements. You should simply rearrange them (and adjust "
                "their indentation as needed)." + reset)
        changed = "Do not change the assignment statements. " + reset
        for assign in assigns:
            self.assertEqual(len(assign.targets), 1, changed)
            variable = assign.targets[0].id
            self.assertIn(variable, ["names", "message"], changed)

        lists = self.find_all(ast.List)
        self.assertEqual(len(lists), 1, "Do not add or remove any list. " +
                reset)
        changed = "Do not change the given list. " + reset
        self.assertEqual(len(lists[0].elts), 3, changed)
        names = tuple([elt.s for elt in lists[0].elts])
        self.assertEqual(names, ("Harry", "Hermione", "Ron"), changed)

        self.assertEqual(len(self.find_all(ast.List, fors[0])), 0, "Do not "
                "initialize the list inside of the for loop. That is "
                "inefficient because it re-initializes the list multiple "
                "times!")

        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 1, "Do not add or remove any function "
                "calls. " + reset)
        changed = "Do not change the print function call. " + reset
        self.assertIsInstance(calls[0].func, ast.Name, changed)
        self.assertEqual(calls[0].func.id, "print", changed)

        calls = self.find_all(ast.Call, fors[0])
        self.assertEqual(len(calls), 1, "The print function call should be "
                "inside of the loop to print each message separately.")

        binops = self.find_all(ast.BinOp, fors[0])
        self.assertEqual(len(binops), 1, "The concatenation operation should "
                "be inside of the for loop. This allows you to create a custom"
                " message for each name.")

        self.exec_solution()
        self.assertEqual(tuple(self.printed_lines),
                ("Hello Harry", "Hello Hermione", "Hello Ron"),
                "You are not printing the right result.")

if __name__ == "__main__":
    unittest.main()
