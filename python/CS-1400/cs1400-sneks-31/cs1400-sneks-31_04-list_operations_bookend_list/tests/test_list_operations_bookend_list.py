import ast
import unittest
import unittest.mock

import asttest

class TestListOperationsBookendList(asttest.ASTTest):

    def setUp(self):
        super().setUp("list_operations_bookend_list.py", False)

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        if any(('def' in line and '[' in line) for line in self.file.split('\n')):
            self.fail("It looks like you added a square bracket on the same "
                    "line as the `def` keyword. Remember, with Python you do "
                    "not indicate the type of a parameter. A parameter only "
                    "has a name; when the function is called, a value (which "
                    "will have a type) will be assigned to it.")

        self.tree = ast.parse(self.file)
        func = self.match_signature("bookend_list", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check the name and parameter and try again.")

        self.assertGreaterEqual(len(self.find_all(ast.Return)), 1, "Don't "
                "forget to return your new list.")
        self.assertGreaterEqual(len(self.find_all(ast.If)), 1, "Remember that "
                "you will need to handle empty lists!")
        self.assertEqual(len(self.find_all(ast.If)), 1, "You should only need "
                "a single if statement.")

        tests = [([], []),
                ([1], [1, 1]),
                ([1,2], [1,2]),
                ([1,2,3], [1,3]),
                (['A', 'B', 'C'], ['A', 'C'])]
        for test in tests:
            with self.subTest(a_list=test[0]):
                from list_operations_bookend_list import bookend_list
                result = bookend_list(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        calls = self.find_function_calls('assert_equal')
        self.assertGreaterEqual(len(calls), 2, "You should test your function "
                "at least twice.")
        self.ensure_coverage(['bookend_list'], .9)

if __name__ == "__main__":
    unittest.main()
