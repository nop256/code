import ast
import unittest

import asttest

msg = "Do not change the behavior of the program."

class TestDocumentingBadLines(asttest.ASTTest):

    def setUp(self):
        super().setUp("documenting_bad_lines.py")

    def test_required_syntax(self):
        assigns = self.find_all(ast.Assign)
        self.assertEqual(len(assigns), 4, msg + " There should be four "
                "assignment statements.")
        vars = [('y', 7), ('x', 3), ('z', 2), ('result', 0)]
        for i in range(len(vars)):
            assign = assigns[i]
            self.assertEqual(len(assign.targets), 1, msg)
            self.assertIsInstance(assign.targets[0], ast.Name, msg)
            self.assertEqual(assign.targets[0].id, vars[i][0], msg)
            if i < 3:
                self.assertIsInstance(assign.value, ast.Num, msg)
                self.assertEqual(assign.value.n, vars[i][1], msg)
            else:
                self.assertIsInstance(assign.value, ast.BinOp, msg)

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(self.printed_lines[0], 349, msg)

if __name__ == "__main__":
    unittest.main()
