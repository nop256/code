import ast
import unittest
import unittest.mock

import asttest

class TestModulesStringOfLetters(asttest.ASTTest):

    def setUp(self):
        super().setUp("modules_string_of_letters.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertNotIn(letters, self.file, "Do not embed the letters string "
                "directly in your program. Use the string module to import the"
                " ascii_letters constant.")

        imports = self.find_all(ast.Import)
        froms = self.find_all(ast.ImportFrom)
        self.assertNotEqual(len(imports + froms), 0,
                "You need to import the string module!")
        found = False
        if imports:
            if not any(alias.name == 'string' for i in imports for alias in i.names):
                self.fail("You need to import the string module.")
            else:
                found = True
        if froms:
            if not found and not any(i.module == 'string' for i in froms):
                self.fail("You need to import the string module.")

        self.assertEqual(len(self.find_all(ast.If)), 0, "Do not use an if "
                "statement to solve this problem. What type of value should "
                "you return? You may find it helpful to review the lesson on "
                "IF statements to see why an IF statement is unnecessary.")
        self.assertEqual(len(self.find_all(ast.For)), 0,
                "Do not use a for loop to solve this problem.")
        self.assertEqual(len(self.find_method_calls("startswith")), 0, "You do"
                " not need the startswith method to solve this problem. It may"
                " seem like it solves this question quickly, but the "
                "startswith method can only check if a string starts with ONE "
                "specific string, not a SET of characters. Another way to "
                "think of this problem is to check if the first character of "
                "the given string is one of the valid letters.")

        func = self.match_signature("starts_with_letter", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        tests = [('ABC', True),
                ('123', False),
                ('!?!?', False),
                ('ABC123', True),
                ('ABC???', True),
                ('1 is A', False),
                ('... Huh', False)]

        for test in tests:
            with self.subTest(word=test[0]):
                from modules_string_of_letters import starts_with_letter
                result = starts_with_letter(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.ensure_coverage(["starts_with_letter"], .5)
        self.assertGreaterEqual(len(self.find_function_calls("assert_equal")),
                2, "You should write at least two unit tests.")

if __name__ == "__main__":
    unittest.main()
