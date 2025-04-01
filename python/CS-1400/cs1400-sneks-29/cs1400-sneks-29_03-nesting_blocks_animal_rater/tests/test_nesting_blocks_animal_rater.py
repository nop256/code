import ast
import unittest
import unittest.mock

import asttest

class TestNestingBlocksAnimalRater(asttest.ASTTest):

    def setUp(self):
        super().setUp("nesting_blocks_animal_rater.py")

    @unittest.mock.patch("sys.stdout")
    def test_rate_animal(self, mock_stdout):
        func = self.match_signature("rate_animal", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check the name and parameter and try again.")
        self.assertFalse(self.function_prints(func), "You should not print "
                "inside of the function, only return the correct rating.")

        returns = self.find_all(ast.Return, func)
        self.assertGreaterEqual(len(returns), 1, "You are not using the "
                "return statement!")

        tests = [("dog", 1),
                ("cat", 2),
                ("capybara", 3),
                ("danger noodle", 4),
                ("", -1),
                ("alpha", -1),
                ("banana", -1)]
        for test in tests:
            with self.subTest(animal=test[0]):
                from nesting_blocks_animal_rater import rate_animal
                result = rate_animal(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        calls = self.find_function_calls('rate_animal')
        self.assertGreaterEqual(len(calls), 1, "You should call `rate_animal` "
                "at least once.")

        calls = self.find_function_calls('print')
        self.assertGreaterEqual(len(calls), 1, "You should print the rating "
                "for you favorite animal.")

if __name__ == "__main__":
    unittest.main()
