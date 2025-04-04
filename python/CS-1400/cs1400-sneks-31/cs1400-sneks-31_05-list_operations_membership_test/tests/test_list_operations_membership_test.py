import ast
import unittest
import unittest.mock

import asttest

class TestListOperationsMembershipTest(asttest.ASTTest):

    def setUp(self):
        super().setUp("list_operations_membership_test.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        func = self.match_signature("is_weekend", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check the name and parameter and try again.")
        self.assertGreaterEqual(len(self.find_all(ast.Return)), 1, "You are "
                "not using the return statement!")

        compares = self.find_all(ast.Compare)
        for compare in compares:
            self.assertEqual(len(compare.ops), 1, "You only need to use the "
                    "`in` operator to check if an item is in a list.")
            self.assertIsInstance(compare.ops[0], ast.In, "You only need to "
                    "use the `in` operator to check if an item is in a list.")
            self.assertNotIsInstance(compare.left, ast.List, "You can't"
                    " compare two things at the same time. You should write a "
                    "separate expression for each day to check if 'Saturday' "
                    "or 'Sunday' is in the list.")

        boolops = self.find_all(ast.BoolOp)
        for boolop in boolops:
            self.assertNotIsInstance(boolop.op, ast.And, "You should not use "
                    "the `and` operator here. Remember you are checking "
                    "whether or not the string `Saturday` *or* the string "
                    "`Sunday` is in the list of days.")

        tests = [(["Monday"], False),
                (["Monday", "Wednesday"], False),
                (["Monday", "Saturday"], True),
                (["Saturday", "Sunday"], True),
                (["Sunday", "Monday"], True),
                (["Monday", "Friday", "Saturday"], True),
                (["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], False)]
        for test in tests:
            with self.subTest(days=test[0]):
                from list_operations_membership_test import is_weekend
                result = is_weekend(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        calls = self.find_function_calls('assert_equal')
        self.assertGreaterEqual(len(calls), 2, "You should test your function "
                "at least twice.")
        self.ensure_coverage(["is_weekend"], .9)

if __name__ == "__main__":
    unittest.main()
