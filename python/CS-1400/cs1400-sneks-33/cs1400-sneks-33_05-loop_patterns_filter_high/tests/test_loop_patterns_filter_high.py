import ast
import unittest
import unittest.mock

import asttest

class TestLoopPatternsFilterHigh(asttest.ASTTest):

    def setUp(self):
        super().setUp("loop_patterns_filter_high.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        #ins_iter.iteration_group()
        #ins_app.append_group()

        func = self.match_signature("filter_high", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Please check its name and parameter and try again.")

        tests = [([1,2,3], [1,2,3], False),
                 ([], [], False),
                 ([40, 50], [40, 50], False),
                 ([40, 50, 60], [40, 50], True),
                 ([60, 70], [], True)]
        for test in tests:
            with self.subTest(a_list=test[0]):
                from loop_patterns_filter_high import filter_high
                result = filter_high(test[0])
                if test[2]:
                    self.assertNotEqual(result, test[0], "You returned the "
                            "original list. Make sure you filter out the "
                            "numbers that are above 50.")
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                2, "You should unit test your function at least twice.")
        self.ensure_coverage(['filter_high'], .9)

if __name__ == "__main__":
    unittest.main()
