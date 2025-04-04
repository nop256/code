import ast
import unittest
import unittest.mock

import asttest

class TestFilesPlusOrMinus(asttest.ASTTest):

    def setUp(self):
        super().setUp("files_plus_or_minus.py")

    @unittest.mock.patch('sys.stdout')
    def test_required_syntax(self, mock_stdout):
        func = self.match_signature('convert_operator', 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        tests = [('+', 1), ('-', -1)]
        for test in tests:
            with self.subTest(a_number=test[0]):
                from files_plus_or_minus import convert_operator
                result = convert_operator(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.ensure_coverage(["convert_operator"], .9)

        self.assertEqual(len(self.find_method_calls('count')), 0, "You "
                "may not use the built-in count method. But good thinking!")
        self.assertEqual(len(self.find_all(ast.ListComp)), 0, "List "
                "comprehensions are not the best way to solve this question, "
                "because we need print as we loop.")
        self.assertEqual(len(self.find_all(ast.List)), 0, "You should not be "
                "creating a new list.")
        self.assertEqual(len(self.find_method_calls("readlines")), 0, "You may"
                " not use the built-in readlines method.")
        self.assertEqual(len(self.find_method_calls("split")), 0, "You do not "
                "need the split method. How do you process a string character "
                "by character?")

        with open("plus_and_minus.txt") as inp:
            values = inp.read()
        total = values.count("+") - values.count("-")
        self.assertNotIn(str(total), self.file, "Do not embed the answer "
                "directly in your program, you should calculate it instead.")

        # Should probably check for this to be within the for loop
        self.assertNotEqual(len(self.find_function_calls('convert_operator')),
                0, "You need to call the convert_operator function.")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0,
            "You are not printing.")
        self.assertEqual(len(self.printed_lines), 1, "You have printed too "
                "many things. Remember, you only need to print the total.")
        self.assertNotIn(self.printed_lines[0], (str(len(values)),
            str(float(len(values)))), "You printed the number of entries.")
        self.assertNotEqual(self.printed_lines, values,
            "You printed the +/- entries, not their total.")
        self.assertEqual(self.printed_lines[0], total,
            "You have printed the wrong answer.")
        self.assertGreaterEqual(len(self.find_function_calls("assert_equal")),
            2, "You should write at least two unit tests.")

if __name__ == "__main__":
    unittest.main()
