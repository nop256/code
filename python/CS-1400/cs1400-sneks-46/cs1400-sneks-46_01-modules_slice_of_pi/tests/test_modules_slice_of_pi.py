import ast
import unittest

import asttest

class TestModulesSliceOfPi(asttest.ASTTest):

    def setUp(self):
        super().setUp("modules_slice_of_pi.py")

    def test_required_syntax(self):
        self.assertNotIn("3.14", self.file, "Do not embed the answer directly "
                "in your program. Use the math module to import the value of pi.")
        self.assertNotIn("3.141592653589793", self.file, "Do not embed the "
                "answer directly in your program. Use the math module to "
                "import the value of pi.")

        imports = self.find_all(ast.Import)
        froms = self.find_all(ast.ImportFrom)
        self.assertNotEqual(len(imports + froms), 0,
                "You need to import the math module!")
        if imports:
            if not any(alias.name == 'math' for i in imports for alias in i.names):
                self.fail("You need to import the math module.")
        if froms:
            if not any(i.module == 'math' for i in froms):
                self.fail("You need to import the math module.")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You need to print.")
        self.assertIn(3.141592653589793, self.printed_lines,
            "You need to print the value of pi.")

if __name__ == "__main__":
    unittest.main()
