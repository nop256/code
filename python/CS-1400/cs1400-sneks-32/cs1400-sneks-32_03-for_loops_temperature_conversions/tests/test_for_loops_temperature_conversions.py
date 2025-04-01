import ast
import unittest

import asttest

class TestForLoopsTemperatureConversions(asttest.ASTTest):

    def setUp(self):
        super().setUp("for_loops_temperature_conversions.py")

    def test_required_syntax(self):
        num_values = [n.n for n in self.find_all(ast.Num)]
        self.assertFalse(any([int(n) in (50, 68, 41) for n in num_values]),
                "It looks like you may have embedded the answer in the code. "
                "Instead, you should calculate the results with the given "
                "formula.")
        self.assertEqual(len(self.find_all(ast.While)), 0,
            "Do not use a while loop. This kind of loop is more useful when "
            "you don't know how many times you need to repeat an operation. In"
            " this case, you know you want to repeat one time for each element"
            " in the list.")

        fors = self.find_all(ast.For)
        self.assertNotEqual(len(fors), 0, "You will need a for loop.")
        self.assertEqual(len(fors), 1, "You will only need one for loop.")
        self.assertEqual(len(self.find_all(ast.List, fors[0])), 0, "Do not "
                "initialize the list inside of the for loop. That is "
                "inefficient because it re-initializes the list multiple "
                "times!")

        lists = self.find_all(ast.List)
        self.assertNotEqual(len(lists), 0, "You will need to create a list.")
        self.assertEqual(len(lists), 1, "You should only have one list.")
        self.assertTrue(all([isinstance(l, ast.Num) for l in lists[0].elts]),
                "Your list should only have numbers in it.")

        assigns = self.find_all(ast.Assign)
        found = False
        for assign in assigns:
            if assign.targets[0].id == 'temperatures':
                if found:
                    self.fail("Do not create another temperatures variable.")
                found = True
                self.assertIsInstance(assign.value, ast.List, "Do not edit the"
                        " temperatures list. Check the starter code and try again.")
                values = [n.n for n in assign.value.elts]
                self.assertEqual(tuple(values), (10, 20, 5), "Do not edit the "
                        "temperatures list. Check the starter code and try again.")

        calls = self.find_all(ast.Call, fors[0])
        print_in_loop = (calls and isinstance(calls[0].func, ast.Name) and calls[0].func.id == "print")
        self.assertTrue(print_in_loop, "The print function call should be "
                "INSIDE of the loop.")
        self.assertGreaterEqual(len(self.find_all(ast.BinOp, fors[0])), 1,
                "The formula should be implemented INSIDE of the loop.")

        self.exec_solution()
        self.assertEqual(tuple(self.printed_lines), (50.0, 68.0, 41.0),
                "You are not printing the right result.")


if __name__ == "__main__":
    unittest.main()
