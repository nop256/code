import ast
import unittest
import unittest.mock

import asttest

class TestNestingBlocksPossiblyUndefined(asttest.ASTTest):

    def setUp(self):
        super().setUp("nesting_blocks_possibly_undefined.py")

    @unittest.mock.patch("sys.stdout")
    def test_calculate_income(self, mock_stdout):
        func = self.match_signature("calculate_income", 1)
        self.assertIsNotNone(func, "Do not change the function's name or "
                "parameter.")

        tests = [(10000, 9000.0),
              (1000, 1000),
              (0, 0),
              (5100, 4590.0)]
        for test in tests:
            with self.subTest(salary=test[0]):
                from nesting_blocks_possibly_undefined import calculate_income
                result = calculate_income(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

            calls = self.find_function_calls('assert_equal')
            self.assertGreaterEqual(len(calls), 2, "You should test your "
                    "function at least 2 times.")
            self.ensure_coverage(["calculate_income"], .9)

if __name__ == "__main__":
    unittest.main()
