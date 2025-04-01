import ast
import unittest

import asttest

class TestForLoopsReplacingInLoops(asttest.ASTTest):

    def setUp(self):
        super().setUp("for_loops_replacing_in_loops.py")

    def test_required_syntax(self):
        fors = self.find_all(ast.For)
        self.assertNotEqual(len(fors), 0, "You will need a for loop.")
        self.assertEqual(len(fors), 1, "You should only need one for loop.")
        self.assertEqual(len(self.find_all(ast.List, fors[0])), 0, "Do not "
                "initialize the List inside of the for loop. That is "
                "inefficient because it re-initializes the list multiple "
                "times!")

        reset = "Do not change the original list. Check the starter code " \
                "and try again."
        filenames = ("All-the-Single-Ladies.mp3", "Call-Me-Maybe.mp3", "Chicken-Dance.mp3")
        lists = self.find_all(ast.List)
        self.assertEqual(len(lists), 1, "You should only have the one list. Do"
                " not remove it either.")
        self.assertEqual(len(lists[0].elts), 3, reset)
        self.assertEqual(set([fname.s for fname in lists[0].elts]),
                set(filenames), reset)

        calls = self.find_all(ast.Call, fors[0])
        f_calls = [c.func.id for c in calls
                   if isinstance(c.func, ast.Name)]
        f_methods = [c.func.attr for c in calls
                     if isinstance(c.func, ast.Attribute)]

        self.assertNotIn("replace", f_calls, "Remember, replace is a method, "
                "not a function! It should be called with .replace after the "
                "filename.")
        self.assertIn("replace", f_methods, "You will need to use the replace "
                "method inside the loop.")
        self.assertIn("print", f_calls, "You will need to use the print "
                "function inside the loop.")

    def test_correct_result(self):
        self.exec_solution()
        right_filenames = ("All the Single Ladies.mp3", "Call Me Maybe.mp3", "Chicken Dance.mp3")
        self.assertNotEqual(len(self.printed_lines), 0, "You are not "
                "printing anything.")
        self.assertEqual(tuple(self.printed_lines), right_filenames, "You are "
                "not printing the correct result.")

if __name__ == "__main__":
    unittest.main()
