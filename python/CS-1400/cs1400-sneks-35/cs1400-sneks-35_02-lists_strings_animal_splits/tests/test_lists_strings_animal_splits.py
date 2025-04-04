import ast
import unittest
import unittest.mock

import asttest

class TestListsStringsAnimalSplits(asttest.ASTTest):

    def setUp(self):
        super().setUp("lists_strings_animal_splits.py", False)

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        if any(('def' in line and '[' in line) for line in self.file.split('\n')):
            self.fail("It looks like you added a square bracket on the same "
                    "line as the def keyword. Remember, with Python you do not"
                    " indicate the type of a parameter. A parameter only has "
                    "a name; when the function is called, a value (which will "
                    "have a type) will be assigned to it.")
        if any(('def' in line and ',' in line) for line in self.file.split('\n')):
            self.fail("It looks like you added a comma on the same line as the"
                    " def keyword. This function only consumes a single "
                    "argument, even if that argument's value contains multiple"
                    " things.")

        self.tree = ast.parse(self.file)

        func = self.match_signature("all_cats", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        self.assertNotEqual(len(self.find_all(ast.For)), 0, "You will need a "
                "FOR loop.")
        conditions = self.find_all(ast.If)
        ands = [bop for bop in self.find_all(ast.BoolOp) if isinstance(bop.op, ast.And)]
        self.assertNotEqual(len(conditions + ands), 0, "You will either need "
                "an IF statement or an AND operator.")
        compares = [c for c in self.find_all(ast.Compare) if
                isinstance(c.ops[0], (ast.In, ast.NotIn))]
        self.assertNotEqual(len(compares), 0, "You will need the IN operator "
                "in your code.")

        tests = [("cat",True),
                ("catfish,fishcat",True),
                ("dog,gerbil", False),
                ("cat,dog,gerbil", False),
                ("cat,cat,gerbil", False),
                ("cat,dog,cat", False)]
        for test in tests:
            with self.subTest(animals=test[0]):
                from lists_strings_animal_splits import all_cats
                result = all_cats(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                1, "You should unit test your function at least once.")
        self.ensure_coverage(['all_cats'], .9)

if __name__ == "__main__":
    unittest.main()
