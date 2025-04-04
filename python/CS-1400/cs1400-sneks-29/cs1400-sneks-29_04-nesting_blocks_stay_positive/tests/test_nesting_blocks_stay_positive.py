import ast
import unittest
import unittest.mock

import asttest

class TestNestingBlocksStayPositive(asttest.ASTTest):

    def setUp(self):
        super().setUp("nesting_blocks_stay_positive.py")

    @unittest.mock.patch("sys.stdout")
    def test_add_positives(self, mock_stdout):
        func = self.match_signature("add_positives", 2)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check the name and parameter and try again.")

        returns = self.find_all(ast.Return, func)
        self.assertGreaterEqual(len(returns), 1, "You are not using the "
                "return statement!")

        tests = [(10, 10, 20),
                  (0, 0, 0),
                  (-10, 5, 0),
                  (5, -10, 0),
                  (-10, -10, 0)]
        for test in tests:
            with self.subTest(a=test[0], b=test[1]):
                from nesting_blocks_stay_positive import add_positives
                result = add_positives(test[0], test[1])
                self.assertEqual(result, test[2], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0:2], result, test[2]))

        calls = self.find_function_calls('assert_equal')
        self.assertGreaterEqual(len(calls), 2, "You should test your function "
                "at least twice.")
        self.ensure_coverage(["add_positives"], .9)

if __name__ == "__main__":
    unittest.main()
