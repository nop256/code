import ast
import unittest
import unittest.mock

import asttest

class TestMutabilityRepeatLouder(asttest.ASTTest):

    def setUp(self):
        super().setUp("mutability_repeat_louder.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        func = self.match_signature('make_exclamations', 1)
        self.assertIsNotNone(func, "Do not change the name or parameters of "
                "the given function.")
        tests = [(['A', 'B'], ['A!', 'B!']),
                (['D', 'E'], ['D!', 'E!']),
                ([], [])]
        for test in tests:
            with self.subTest(message=test[0]):
                from mutability_repeat_louder import make_exclamations
                result = make_exclamations(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()
