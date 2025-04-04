import ast
import unittest
import unittest.mock

import asttest

class TestLoopPatternsMaximumOdd(asttest.ASTTest):

    def setUp(self):
        super().setUp("loop_patterns_maximum_odd.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        func = self.match_signature("is_odd", 1)
        self.assertIsNotNone(func, "Do not change or remove the is_odd "
                "function. Please fix it based on the starter code and try "
                "again.")

        func = self.match_signature("maximum_odd", 1)
        self.assertGreaterEqual(len(self.find_all(ast.If, func)), 1, "You "
                "will need a single if statement.")
        self.assertGreaterEqual(len(self.find_all(ast.For, func)), 1, "You "
                "will need a single for loop.")

        tests = [(1, True),
                (0, False),
                (2, False),
                (3, True)]
        for test in tests:
            with self.subTest(a_number=test[0]):
                from loop_patterns_maximum_odd import is_odd
                result = is_odd(test[0])
                self.assertEqual(result, test[1], "Do not change the is_odd "
                        "function. Please fix it based on the starter code and"
                        "try again.")

        tests = [([1,2,3,4], 3),
                ([3,2,1,4], 3),
                ([2, 3, 1,4], 3),
                ([5, 5, 5], 5),
                ([0, 0, 2,1], 1)]
        for test in tests:
            with self.subTest(a_list=test[0]):
                from loop_patterns_maximum_odd import maximum_odd
                result = maximum_odd(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        # TODO: Should probably try harder to confirm they tested is_odd
        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                3, "You should unit test your function at least three times.")
        self.ensure_coverage(['is_odd', 'maximum_odd'], .9)

if __name__ == "__main__":
    unittest.main()
