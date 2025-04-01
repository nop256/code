import ast
import io
import unittest
import unittest.mock

import asttest

class TestFilesFixNames(asttest.ASTTest):

    def setUp(self):
        super().setUp("files_fix_names.py")

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
        self.assertNotEqual(len(self.find_method_calls("split")), 0,
                "You will need to call the split method.")

        stripping = (self.find_method_calls('strip') +
                self.find_method_calls('rstrip'))
        self.assertNotEqual(len(stripping), 0, "Make sure you are stripping "
                "the whitespace from the file's lines!")

        case = (self.find_method_calls("upper") +
                self.find_method_calls("lower"))
        self.assertEqual(len(case), 0,
                "Do not forget to fix the capitalization with capitalize!")
        self.assertNotEqual(len(self.find_method_calls("capitalize")), 0,
                "Do not forget to fix the capitalization with .capitalize()!")

        originals = ["washington,george",
                "hamilton,alexander",
                "franklin,benjamin",
                "adams,john",
                "adams,samuel",
                "jefferson,thomas",
                "madison,james",
                "jay,john"]
        values = ["George Washington",
                "Alexander Hamilton",
                "Benjamin Franklin",
                "John Adams",
                "Samuel Adams",
                "Thomas Jefferson",
                "James Madison",
                "John Jay"]

        for name in values:
            self.assertNotIn(name, self.file, "Do not embed the answer in your"
                    " program. If there were thousands of names, would you "
                    "even have time to do that?")

        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            import files_fix_names
            result = mock_stdout.getvalue().strip().split('\n')
            self.assertNotEqual(len(result), 0,
                    "You are not printing.")
            if len(values) in result or float(len(values)) in result:
                self.fail("You printed the number of names.")
            self.assertGreaterEqual(len(result), len(values), "You "
                    "have printed too few things. Make sure you are printing each "
                    "name on its own line")
            self.assertEqual(len(result), len(values),
                    "You are printing too many things.")
            self.assertNotEqual(result, originals, "You have printed "
                    "the original values instead of the modified names.")
            self.assertEqual(result, values,
                    "You have printed the wrong answer.")

if __name__ == "__main__":
    unittest.main()
