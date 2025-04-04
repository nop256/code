import ast
import io
import unittest
import unittest.mock

import asttest

class TestForLoopsFunctionWithFor(asttest.ASTTest):

    def setUp(self):
        super().setUp("for_loops_function_with_for.py", False)

    def test_required_syntax(self):
        if any(('def' in line and '[' in line) for line in self.file.split('\n')):
            self.fail("It looks like you added a square bracket on the same "
                    "line as the def keyword. Remember, parameters are simply "
                    "variable names and, with Python, you do not indicate the "
                    "type of a parameter. A parameter only has a name; when "
                    "the function is called, a value (which will have a type) "
                    "will be assigned to it.")

        self.tree = ast.parse(self.file)

        num_values = [n.n for n in self.find_all(ast.Num)]
        if any([int(n) in (50, 86, 104) for n in num_values]):
            self.fail("It looks like you may have embedded the answer in the "
                    "code. You should instead implement a function to "
                    "calculate the correct temperature values.")

        self.assertEqual(len(self.find_all(ast.While)), 0, "Do not use a while"
                " loop.")

        functions = self.find_all(ast.FunctionDef)
        self.assertNotEqual(len(functions), 0, "You must define a function.")

        func = self.match_signature("print_fahrenheit", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        fors = self.find_all(ast.For, func)
        self.assertNotEqual(len(fors), 0, "You need to use a for loop inside "
                "of your function.")

        calls = self.find_function_calls('print_fahrenheit')
        self.assertGreaterEqual(len(calls), 1,
            "You must call print_fahrenheit with the list [20, 30, 40]. Do not"
            " change the starter code, simply add your function definition to it.")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_correct_result(self, mock_stdout1):
        import for_loops_function_with_for
        self.assertEqual("68.0\n86.0\n104.0\n", mock_stdout1.getvalue(), "You "
                "are not printing the correct result.")

        tests = [([40, 30, 20], "104.0\n86.0\n68.0\n")]
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                with self.subTest(temperatures=test[0]):
                    from for_loops_function_with_for import print_fahrenheit
                    result = print_fahrenheit(test[0])
                    printed = mock_stdout.getvalue()
                    self.assertEqual(result, None, "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0], result, None))
                    self.assertEqual(printed, test[1], "Your function is not "
                            "printing the correct result. When given '{}' it "
                            "printed '{}', however, it should have printed "
                            "'{}'.".format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()
