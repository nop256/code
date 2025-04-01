import ast
import unittest
import unittest.mock

import asttest

class TestNestingBlocksRedundantIf(asttest.ASTTest):

    def setUp(self):
        super().setUp("nesting_blocks_redundant_if.py")

    @unittest.mock.patch("sys.stdout")
    def test_am_i_on_fire(self, mock_stdout):
        ifs = self.find_all(ast.If)
        compares = self.find_all(ast.Compare)
        compare_ops = [type(op) for compare in compares for op in compare.ops]

        self.assertEqual(len(ifs), 0, "You should refactor the function so "
                "that it no longer uses an `if` statement.")
        self.assertNotIn(ast.Eq, compare_ops, "You should not need to use "
                "`==` to solve this problem.")
        self.assertNotIn(ast.NotEq, compare_ops, "You should not need to use "
                "`!=` to solve this problem.")

        func = self.match_signature("am_i_on_fire", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check the name and parameter and try again.")

        returns = self.find_all(ast.Return, func)
        self.assertGreaterEqual(len(returns), 1, "You are not using the "
                "return statement!")

        tests = [(100, False),
                  (110, True),
                  (0, False)]
        for test in tests:
            with self.subTest(temperature=test[0]):
                from nesting_blocks_redundant_if import am_i_on_fire
                result = am_i_on_fire(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        calls = self.find_function_calls('assert_equal')
        self.assertGreaterEqual(len(calls), 2, "You should test your function "
                "at least twice.")
        self.ensure_coverage(["am_i_on_fire"], .9)

if __name__ == "__main__":
    unittest.main()
