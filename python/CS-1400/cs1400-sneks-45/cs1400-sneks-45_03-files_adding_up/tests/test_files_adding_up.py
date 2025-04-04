import ast
import unittest

import asttest

class TestFilesAddingUp(asttest.ASTTest):

    def setUp(self):
        super().setUp("files_adding_up.py")

    def test_required_syntax(self):
        self.assertNotEqual(len(self.find_function_calls("open")), 0, "You "
                "need to *open* the file.")
        self.assertNotEqual(len(self.find_method_calls("close")), 0, "Don't "
                "forget to close the file!")

        self.assertEqual(len(self.find_all(ast.ListComp)), 0, "List "
                "comprehensions are not the best way to solve this question, "
                "because we need print as we loop.")
        self.assertEqual(len(self.find_all(ast.List)), 0, "You should not be "
                "creating a new list.")
        self.assertEqual(len(self.find_method_calls("read")), 0, "You may not "
                "use the built-in read method.")
        self.assertEqual(len(self.find_method_calls("readlines")), 0, "You may"
                " not use the built-in readlines method.")

        fors = self.find_all(ast.For)
        self.assertNotEqual(len(fors), 0, "You need to use a for loop.")
        self.assertEqual(len(fors), 1, "You only need one for loop.")

        rainfall_file = open("rainfall.txt")
        values = [float(line) for line in rainfall_file]
        rainfall_file.close()
        total = sum(values)
        self.assertNotIn(str(total), self.file, "Do not embed the answer "
                "directly in your program, you should calculate it instead.")
        self.assertNotEqual(len(self.find_function_calls('float')), 0,
            "Make sure you convert each string to a float!")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0,
            "You are not printing.")
        self.assertEqual(len(self.printed_lines), 1, "You have printed too "
                "many things. Remember, you only need to print the total "
                "rainfall.")
        self.assertNotIn(self.printed_lines[0], (len(values),
            str(float(len(values)))), "You printed the number of entries "
            "instead of the total rainfall.")
        self.assertNotEqual(values, self.printed_lines, "You printed the "
                "rainfall values, not their total.")
        self.assertEqual(self.printed_lines[0], total,
            "You have printed the wrong answer.")

if __name__ == "__main__":
    unittest.main()
