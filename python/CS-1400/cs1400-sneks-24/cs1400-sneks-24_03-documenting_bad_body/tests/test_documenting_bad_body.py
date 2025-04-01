import ast
import unittest
import unittest.mock

import asttest

class TestDocumentingBadBody(asttest.ASTTest):

    def setUp(self):
        super().setUp("documenting_bad_body.py")

    def test_required_syntax(self):
        func = self.match_signature("force_palindrome", 1)
        self.assertIsNotNone(func, "The function definition has changed. Do "
                "not change the original function definition other than the "
                "docstring.")
        self.assertFalse(self.function_prints(func), "Your function is "
                "printing. This function is not supposed to print - you are "
                "supposed to print its result OUTSIDE the function "
                "definition.")
        self.assertGreaterEqual(len(self.find_all(ast.Return)), 1, "Your "
                "function is not returning. It should be returning a value!")
        self.assertGreaterEqual(len(self.find_function_calls('print')), 1,
                "You need to print outside the function.")

    def test_correct_result(self):
        tests = [('AB', 'ABBA'), ('Dog', 'DoggoD'), ('', '')]
        for test in tests:
            with unittest.mock.patch('sys.stdout') as buffer:
                with self.subTest(a_word=test[0]):
                    from documenting_bad_body import force_palindrome
                    result = force_palindrome(test[0])
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()
