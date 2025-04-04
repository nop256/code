import ast
import unittest
import unittest.mock

import asttest

class TestLoopPatternsSumHigh(asttest.ASTTest):

    def setUp(self):
        super().setUp("loop_patterns_sum_high.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        #ins_cont.missing_zero_initialization()
        #ins_cont.missing_no_print()
        #ins_cont.missing_summing_list()

        func = self.match_signature("sum_high", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Please check its name and parameter and try again.")

        tests = [([1,2,3], 0, True),
                ([30, 40, 50, 60, 70], 130, True),
                ([50, 50, 50], 0, True),
                ([1, 60, 100], 160, True),
                ([100, 100], 200, False)]
        for test in tests:
            with self.subTest(a_list=test[0]):
                from loop_patterns_sum_high import sum_high
                result = sum_high(test[0])
                if test[2]:
                    self.assertNotEqual(result, sum(test[0]), "You summed the "
                            "entire list. Make sure you only add the numbers that "
                            "are above 50.")
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                2, "You should unit test your function at least twice.")
        self.ensure_coverage(['sum_high'], .9)

if __name__ == "__main__":
    unittest.main()
