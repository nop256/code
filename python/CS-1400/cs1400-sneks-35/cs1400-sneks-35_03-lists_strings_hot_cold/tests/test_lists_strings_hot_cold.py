import ast
import unittest
import unittest.mock

import asttest

class TestListsStringsHotCold(asttest.ASTTest):

    def setUp(self):
        super().setUp("lists_strings_hot_cold.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        func = self.match_signature("add_hot_cold", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        self.assertEqual(len(self.find_method_calls('count')), 0, "Do not "
                "use the .count() method.")
        self.assertNotEqual(len(self.find_all(ast.For)), 0, "You will need a "
                "FOR loop.")
        self.assertEqual(len(self.find_function_calls("split")), 0, "You will "
                "not need the .split() method. How do you iterate over a "
                "string character-by-character?")

        tests = [("", 0),
                ("HHHH",4),
                ("CCCC", -4),
                ("HCHC", 0),
                ("HHHC", 2),
                ("CCCH", -2)]
        for test in tests:
            with self.subTest(temperatures=test[0]):
                from lists_strings_hot_cold import add_hot_cold
                result = add_hot_cold(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                1, "You should unit test your function at least once.")
        self.ensure_coverage(['add_hot_cold'], .9)

if __name__ == "__main__":
    unittest.main()
