import ast
import unittest

import asttest

class TestForLoopsToYourCredit(asttest.ASTTest):

    def setUp(self):
        super().setUp("for_loops_to_your_credit.py")

    def test_required_syntax(self):
        self.assertEqual(len(self.find_all(ast.While)), 0, "Do not use a while"
                " loop. This kind of loop is more useful when you don't know "
                "how many times you need to repeat an operation. In this case,"
                " you know you want to repeat one time for each element in the"
                " list.")

        fors = self.find_all(ast.For)

        self.assertNotEqual(len(fors), 0, "You will need to use a for loop.")
        self.assertEqual(len(fors), 1, "You will only need one for loop.")
        self.assertEqual(len(self.find_all(ast.List, fors[0])), 0, "Do not "
                "initialize the List inside the for loop. That is inefficient,"
                " because it re-initializes the list multiple times!")

        lists = self.find_all(ast.List)
        self.assertNotEqual(len(lists), 0, "You will need to create a list.")
        self.assertEqual(len(lists), 1, "You should only have one list.")
        self.assertTrue(any([isinstance(l, ast.Num) for l in lists[0].elts]),
                "Your list should only have numbers in it.")

        calls = self.find_all(ast.Call, fors[0])
        if not (len(calls) > 0 and isinstance(calls[0].func, ast.Name)
            and calls[0].func.id == "print"):
            self.fail("The print function should be called INSIDE of the loop.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertGreaterEqual(len(self.printed_lines), 1, "You are not "
            "printing anything.")
        self.assertFalse(any([isinstance(l, list) for l in self.printed_lines]),
            "You should be printing out individual elements, not the entire "
            "list.")

if __name__ == "__main__":
    unittest.main()
