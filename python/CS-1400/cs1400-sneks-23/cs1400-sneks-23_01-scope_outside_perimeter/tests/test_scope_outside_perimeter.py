import ast
import io
import unittest
import unittest.mock

import asttest

class TestScopeOutsidePerimeter(asttest.ASTTest):

    def setUp(self):
        super().setUp("scope_outside_perimeter.py")

    def test_required_syntax(self):
        funcdefs = self.find_all(ast.FunctionDef)
        self.assertEqual(len(funcdefs), 1, "You should define exactly one "
                "function.")
        self.assertEqual(funcdefs[0].name, "calculate_perimeter", "You did not"
                " define the 'calculate_perimeter' function correctly.")
        self.assertFalse(self.function_prints(funcdefs[0]), "Your function is "
                "printing. This function is not supposed to print.")
        self.assertIsNotNone(self.match_signature("calculate_perimeter", 2),
                "You did not define the function correctly. Check its name and"
                " parameters and try again.")
        self.assertNotEqual(len(self.find_all(ast.Return)), 0, "Your function "
                "is not returning. It should return a value!")

    def test_correct_result(self):
        tests = [(2, 3, 10), (0, 0, 0), (3, 2, 10)]
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                with self.subTest(width=test[0], height=test[1]):
                    from scope_outside_perimeter import calculate_perimeter
                    result = calculate_perimeter(test[0], test[1])
                    printed = buffer.getvalue()
                    self.assertNotIn("FAILURE", printed, "\n\nThe unit test is"
                            " not passing: \n\n{}".format(printed))
                    self.assertEqual(result, test[2], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0:2], result, test[2]))

if __name__ == "__main__":
    unittest.main()
