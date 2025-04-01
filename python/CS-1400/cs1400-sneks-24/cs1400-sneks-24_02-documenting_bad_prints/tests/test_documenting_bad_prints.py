import ast
import unittest

import asttest

class TestDocumentingBadPrints(asttest.ASTTest):

    def setUp(self):
        super().setUp("documenting_bad_prints.py")

    def test_required_syntax(self):
        prints = ['''print("First, we'll assign some variables.")''',
                '''print("Then, we'll join the string variables together.")''',
                '''print("Next, we can join the name and age.")''',
                '''print("Then we will print out the result.")''']
        for p in prints:
            self.assertIn(p, self.file, "Do not delete or change any of the "
                    "print function calls other than commenting them out.")
            self.assertEqual(len(self.find_function_calls("print")), 1, "You "
                    "did not comment out the correct number of print function "
                    "calls.")

        msg = "You should only comment out print functions. Do not change the rest of the program."
        assigns = self.find_all(ast.Assign)
        self.assertEqual(len(assigns), 5, msg + "There should be five "
                "assignment statements.")
        vars = [("name", "Klaus"), ("title", "Dr."), ("age", 17), ("full_name", "Dr. Klaus"), ("full_message", "Dr. Klaus's age is 17")]
        for i in range(len(vars)):
            assign = assigns[i]
            self.assertEqual(len(assign.targets), 1, msg)
            self.assertIsInstance(assign.targets[0], ast.Name, msg)
            self.assertEqual(assign.targets[0].id, vars[i][0], msg)
            if i == 2:
                self.assertIsInstance(assign.value, ast.Num, msg)
                self.assertEqual(assign.value.n, vars[i][1], msg)
            elif i < 3:
                self.assertIsInstance(assign.value, ast.Str, msg)
                self.assertEqual(assign.value.s, vars[i][1], msg)
            else:
                self.assertIsInstance(assign.value, ast.BinOp, msg)

if __name__ == "__main__":
    unittest.main()
