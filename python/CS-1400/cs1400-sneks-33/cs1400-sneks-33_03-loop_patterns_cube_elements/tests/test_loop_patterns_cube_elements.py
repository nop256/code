import ast
import unittest
import unittest.mock

import asttest

class TestLoopPatternsCubeElements(asttest.ASTTest):

    def setUp(self):
        super().setUp("loop_patterns_cube_elements.py", False)

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        self.assertNotIn("^", self.file, "Remember, the ^ operator is not used"
                " as the exponent operator in Python.")
        self.tree = ast.parse(self.file)

        binops = self.find_all(ast.BinOp)
        augs = self.find_all(ast.AugAssign)
        for binop in binops+augs:
            self.assertNotIsInstance(binop.op, ast.Add, "You shouldn't add "
                    "elements using the + operator. Instead, you should use "
                    "the .append() method.")

        func =  self.match_signature("cube_elements", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Please check its name and parameter and try again.")

        from loop_patterns_cube_elements import cube_elements
        test = [1,2,3]
        result = cube_elements(test)
        self.assertNotEqual(result, 6, "You have summed the list instead of "
                "cubing each element.")
        self.assertNotEqual(result, test, "You are not producing a new, "
                "modified list with cubed values.")

        tests = [([1,2,3], [1,8,27]),
                ([1], [1]),
                ([4, 4, 4], [64, 64, 64]),
                ([0], [0]),
                ([], [])]
        for test in tests:
            with self.subTest(a_list=test[0]):
                result = cube_elements(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                2, "You should unit test your function at least twice.")
        self.ensure_coverage(['cube_elements'], .9)

if __name__ == "__main__":
    unittest.main()
