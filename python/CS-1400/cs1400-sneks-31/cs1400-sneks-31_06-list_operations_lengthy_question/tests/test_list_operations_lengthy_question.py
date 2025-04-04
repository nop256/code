import ast
import unittest
import unittest.mock

import asttest

class TestListOperationsLengthyQuestion(asttest.ASTTest):

    def setUp(self):
        super().setUp("list_operations_lengthy_question.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        func = self.match_signature("check_length", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        self.assertGreaterEqual(len(self.find_all(ast.Return)), 1, "You are "
                "not using a return statement!")
        self.assertGreaterEqual(len(self.find_function_calls("len")), 1, "You "
                "must use the `len` built-in function.")

        tests = [([], False),
            ([1], False),
            ([1,2], False),
            ([1,2,3], True),
            ([1,2,3,4], True),
            ([1,2,3,4,5], True),
            ([1,2,3,4,5,6], False)]
        for test in tests:
            with self.subTest(a_list=test[0]):
                from list_operations_lengthy_question import check_length
                result = check_length(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))


        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                2, "You should test your function at least twice.")
        self.ensure_coverage(["check_length"], .9)

if __name__ == "__main__":
    unittest.main()
