import ast
import io
import unittest
import unittest.mock

import asttest

class TestScopeWeekendOff(asttest.ASTTest):

    def setUp(self):
        super().setUp("scope_weekend_off.py")

    def test_required_syntax(self):
        funcdefs = self.find_all(ast.FunctionDef)
        self.assertEqual(len(funcdefs), 1, "You should define exactly one "
                "function.")
        self.assertEqual(funcdefs[0].name, "cut_day", "You did not define the "
                "'cut_day' function correctly.")
        self.assertFalse(self.function_prints(funcdefs[0]), "Your function is "
                "printing. This function is not supposed to print.")
        self.assertIsNotNone(self.match_signature("cut_day", 0), "You "
                "implemented the function incorrectly. Check its name and "
                "parameters and try again.")
        self.assertGreaterEqual(len(self.find_all(ast.Return)), 0, "Your "
                "function is not returning. It should return a value!")
        self.assertGreaterEqual(len(self.find_function_calls('print')), 1,
                "You need to print outside of the function.")
        self.assertGreaterEqual(len(self.find_function_calls('input')), 1,
                "Do not delete the input function call! However, you will want"
                " to move it somewhere else in the program.")

    @unittest.mock.patch('builtins.input', side_effect=["saturday", "saturday", "monday"])
    @unittest.mock.patch('sys.stdout')
    def test_correct_result(self, mock_stdout, mock_input):
        mock_stdins = ["saturday", "saturday", "monday"]
        results = ["satur", "satur", "mon"]
        import scope_weekend_off
        for i in range(1, len(mock_stdins)):
            with self.subTest(day_of_week=mock_stdins[i]):
                result = scope_weekend_off.cut_day()
                self.assertEqual(result, results[i], "Your function is not "
                        "returning the correct result. When the user "
                        "typed '{}' it returned '{}', however, it "
                        "should have returned '{}'."
                        .format(mock_stdins[i], result, results[i]))

if __name__ == "__main__":
    unittest.main()
