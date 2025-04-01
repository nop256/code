import ast
import unittest
import unittest.mock

import asttest

class TestNestingBlocksDrinkingFunction(asttest.ASTTest):

    def setUp(self):
        super().setUp("nesting_blocks_renting_function.py")

    @unittest.mock.patch('sys.stdout')
    def test_can_rent(self, mock_stdout):
        func = self.match_signature("can_rent", 2)
        self.assertIsNotNone(func, "You did not define the function "
                "correctly. Check its name and parameters and try again.")

        returns = self.find_all(ast.Return, func)
        self.assertGreaterEqual(len(returns), 1, "You are not using the return"
                " statement!")
        self.assertEqual(len(returns), 4, "You are not using the correct "
                "number of return statements.")

        tests = [(20, True, "Too young"),
                (21, True, "Can rent a car"),
                (21, False, "Doesn't have a license"),
                (999, True, "Can rent a car"),
                (999, False, "Doesn't have a license"),
                (1000, True, "Too old")]
        for test in tests:
            with self.subTest(age=test[0], has_license=test[1]):
                    from nesting_blocks_renting_function import can_rent
                    result = can_rent(test[0], test[1])
                    self.assertEqual(result, test[2], "Your function is "
                            "not returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned '{}'."
                            .format(test[0:2], result, test[2]))

        calls = self.find_function_calls("assert_equal")
        self.assertGreaterEqual(len(calls), 4, "You did not write enough unit "
                "tests.")

        self.ensure_coverage(['can_rent'], .9)

if __name__ == "__main__":
    unittest.main()
