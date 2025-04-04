import ast
import io
import unittest
import unittest.mock
import importlib

import asttest

class TestListsStringsSumUserInput(asttest.ASTTest):

    def setUp(self):
        super().setUp("lists_strings_sum_user_input.py")

    @unittest.mock.patch('sys.stdout')
    @unittest.mock.patch('builtins.input')
    def test_required_syntax(self, mockin, mockout):
        self.assertNotEqual(len(self.find_all(ast.For)), 0, "You will need a "
                "for loop.")
        self.assertEqual(len(self.find_all(ast.FunctionDef)), 0, "Do not "
                "define any functions.")

        inputs = self.find_function_calls("input")
        self.assertNotEqual(len(inputs), 0, "You need to call the input() "
                "function once.")
        self.assertEqual(len(inputs), 1, "You should not call the input() "
                "function more than once.")

        splits = self.find_method_calls("split")
        self.assertNotEqual(len(splits), 0, "You need to call the split() "
                "method once.")
        self.assertEqual(len(splits), 1, "You should not call the split() "
                "method more than once.")

        prints = self.find_function_calls("print")
        self.assertNotEqual(len(prints), 0, "You need to call the print() "
                "function once.")
        self.assertEqual(len(prints), 1, "You should not call the print() "
                "function more than once.")

        import lists_strings_sum_user_input
        for mock_stdin, result in [("10,20,30", "60"), ("30,40", "70"), ("0", "0")]:
            with self.subTest(user_input=mock_stdin):
                with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout, \
                        unittest.mock.patch('builtins.input', side_effect=[mock_stdin]):
                    importlib.reload(lists_strings_sum_user_input)
                    printed = mock_stdout.getvalue().strip()
                    self.assertNotEqual(len(printed), 0, "Your "
                            "program does not seem to print anything if the "
                            "input {} is typed by the user."
                            .format(repr(mock_stdin)))
                    self.assertEqual(printed, result, "Your program "
                            "is not printing the correct result. When the user "
                            "typed {} it printed {}, however, it should have "
                            "printed {}."
                            .format(repr(mock_stdin), repr(printed), repr(result)))

if __name__ == "__main__":
    unittest.main()
