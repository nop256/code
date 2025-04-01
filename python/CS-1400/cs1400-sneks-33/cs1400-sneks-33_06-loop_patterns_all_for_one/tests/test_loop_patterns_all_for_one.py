import ast
import unittest
import unittest.mock

import asttest

class TestLoopPatternsAllForOne(asttest.ASTTest):

    def setUp(self):
        super().setUp("loop_patterns_all_for_one.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        self.assertEqual(len(self.find_all(ast.If)), 0, "You can't use any IF "
                "statements! You don't need them. Remember, boolean values can"
                " be used in expression just like ints and floats.")
        for b in self.find_all(ast.Compare):
            for o in b.ops:
                if isinstance(o, (ast.In, ast.NotIn)):
                    self.fail("Good thought, but you cannot use the in "
                            "operator for this problem.")

        self.assertEqual(len(self.find_function_calls("contains")), 0, "You "
               "cannot use the contains method. But good thought!")
        self.assertEqual(len(self.find_function_calls("index")), 0, "You "
               "cannot use the index method. But good thought!")

        func = self.match_signature("all_true", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Please check its name and parameter and try again.")

        tests = [([], True),
                ([True], True),
                ([False], False),
                ([True, True, True], True),
                ([False, False, False], False),
                ([True, True, False], False)]
        for test in tests:
            with self.subTest(a_list=test[0]):
                from loop_patterns_all_for_one import all_true
                result = all_true(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                2, "You should unit test your function at least twice.")
        self.ensure_coverage(['all_true'], .9)

if __name__ == "__main__":
    unittest.main()
