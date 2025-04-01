import ast
import unittest

import asttest

class TestFilesRedacted(asttest.ASTTest):

    def setUp(self):
        super().setUp("files_redacted.py")

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

        stripping = (self.find_method_calls('strip') +
                self.find_method_calls('rstrip'))
        self.assertNotEqual(len(stripping), 0, "Make sure you are stripping "
                "the new lines before you print!")

        messages = open('messages.txt')
        unredacted_answer = [l.strip() for l in messages]
        messages.close()
        self.exec_solution()
        self.assertFalse(any(l.endswith('\n') for l in self.printed_lines),
            "Make sure you are stripping the new lines before you print!")
        answer= [r.replace('James Bond', '[Redacted]') for r in unredacted_answer]
        self.assertLessEqual(len(self.printed_lines), len(answer),
            "You have printed too many things.")
        self.assertNotEqual(len(self.printed_lines), 1, "You have not printed "
                "enough things. Is it possible you're printing everything on "
                "one line?")
        self.assertEqual(len(self.printed_lines), len(answer),
                "You have not printed enough things.")
        self.assertNotEqual(self.printed_lines, unredacted_answer,
            "You have not redacted the name 'James Bond'.")
        self.assertEqual(self.printed_lines, answer,
            "You have not printed the right things.")

if __name__ == "__main__":
    unittest.main()
