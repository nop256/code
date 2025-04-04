import ast
import unittest
import unittest.mock

import asttest

class TestLoopPatternsMinimum(asttest.ASTTest):

    def setUp(self):
        super().setUp("loop_patterns_minimum.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        self.assertEqual(len(self.find_all(ast.If)), 1, "You will need a "
                "single if statement.")
        self.assertEqual(len(self.find_all(ast.For)), 1, "You will need a "
                "single for loop.")

        func = self.match_signature("minimum", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Please check its name and parameter and try again.")

        tests = [([1,2,3], 1),
                ([3,2,1], 1),
                ([2, 3, 1], 1),
                ([5, 5, 5], 5),
                ([0, 0, 2], 0)]
        for test in tests:
            with self.subTest(a_list=test[0]):
                from loop_patterns_minimum import minimum
                result = minimum(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                2, "You should unit test your function at least twice.")
        self.ensure_coverage(['minimum'], .9)

if __name__ == "__main__":
    unittest.main()
