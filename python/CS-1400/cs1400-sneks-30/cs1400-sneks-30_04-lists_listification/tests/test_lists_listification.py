import ast
import unittest
import unittest.mock

import asttest

class TestListsListification(asttest.ASTTest):

    def setUp(self):
        super().setUp("lists_listification.py")

    @unittest.mock.patch("sys.stdout")
    def test_make_list(self, mock_stdout):
        func = self.match_signature("make_list", 3)
        self.assertIsNotNone(func, "You did not define your function "
                "correctly. Check its name and parameters and try again.")

        returns = self.find_all(ast.Return, func)
        self.assertNotEqual(len(returns), 0, "You are not using the return "
                "statement in your function!")
        lists = len(self.find_all(ast.List, func)) + len(self.find_function_calls("list"))
        if lists < 1:
            self.fail("You must create a list.")
        elif lists > 1:
            self.fail("You should only have one list.")

        tests = [(1, 2, 3, [1,2,3]),
                  ("First", "Second", "Third", ["First", "Second", "Third"]),
                  (True, False, True, [True, False, True])]
        for test in tests:
            with self.subTest(a=test[0], b=test[1], c=test[2]):
                from lists_listification import make_list
                result = make_list(test[0], test[1], test[2])
                self.assertEqual(result, test[3], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0:3], result, test[3]))

        calls = self.find_function_calls('make_list')
        if len(calls) < 1:
            self.fail("You should call `make_list`.")
        calls = self.find_function_calls('assert_equal')
        if len(calls) < 1:
            self.fail("You should test your function at least once.")
        self.ensure_coverage(["make_list"], .9)

if __name__ == "__main__":
    unittest.main()
