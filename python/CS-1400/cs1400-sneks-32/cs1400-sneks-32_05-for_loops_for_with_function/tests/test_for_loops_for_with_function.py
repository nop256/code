import ast
import io
import unittest
import unittest.mock

import asttest

class TestForLoopsForWithFunction(asttest.ASTTest):

    def setUp(self):
        super().setUp("for_loops_for_with_function.py", False)

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
        if any([int(n) in (50, 68, 86) for n in num_values]):
            self.fail("It looks like you may have embedded the answer in the "
                    "code. You should instead implement a function to "
                    "calculate the correct temperature values.")

        self.assertEqual(len(self.find_all(ast.While)), 0, "Do not use a while"
                " loop.")

        functions = self.find_all(ast.FunctionDef)
        self.assertNotEqual(len(functions), 0, "You must define a function.")

        func = self.match_signature("convert_fahrenheit", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        returns = self.find_all(ast.Return, func)
        self.assertNotEqual(len(returns), 0, "You should return the result from "
                "your function.")

        fors = self.find_all(ast.For, func)
        self.assertEqual(len(fors), 0, "Your function definition should not "
                "have a for loop in it.")

        calls = self.find_function_calls('convert_fahrenheit')
        self.assertGreaterEqual(len(calls), 1, "You should call "
                "convert_fahrenheit three times with the temperatures 10, 20, "
                "and 30.")

        fors = self.find_all(ast.For)
        self.assertNotEqual(len(fors), 0, "You will need a for loop, just not "
                "inside of the function.")

        calls = [c.func.id for c in self.find_all(ast.Call, fors[0])
                if isinstance(c.func, ast.Name)]
        self.assertIn("print", calls, "You will need to print the converted "
                "temperature inside of the for loop.")
        self.assertIn("convert_fahrenheit", calls, "You will need to call "
                "your convert_fahrenheit function in the for loop.")

        calls = self.find_function_calls('convert_fahrenheit')
        self.assertNotEqual(len(calls), 0, "You should call convert_fahrenheit"
                " once.")
        self.assertEqual(len(calls), 1, "You should call convert_fahrenheit "
                "only once.")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_correct_result(self, mock_stdout1):
        import for_loops_for_with_function
        self.assertEqual("50.0\n68.0\n86.0\n", mock_stdout1.getvalue(), "You "
                "are not printing the correct result.")

        tests = [(10, 50.0),
                 (20, 68.0),
                 (30, 86.0),
                 (5, 41.0)]
        for test in tests:
            with self.subTest(temperature=test[0]):
                from for_loops_for_with_function import convert_fahrenheit
                result = convert_fahrenheit(test[0])
                self.assertEqual(result, test[1], "Your function is not "
                        "returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned "
                        "'{}'.".format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()
