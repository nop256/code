import ast
import sys
import unittest

import asttest

class TestSurveyResults(asttest.ASTTest):

    def setUp(self):
        super().setUp("survey_results.py")

    def test_variables(self):
        assigns = self.find_all(ast.Assign)
        if len(assigns) < 1:
            self.fail("You must use an assignment statement to create a "
                    "variable to hold your survey responses and other "
                    "information.")
        elif len(assigns) > 4:
            self.fail("You should only have four assignment statements.")

        types = {
                "QUESTION": ast.Str,
                "ANSWERS": ast.List,
                "NAME": ast.Str,
                "PLEDGE": ast.Str
                }

        if sys.version_info >= (3, 8):
            types = {
                    "QUESTION": str,
                    "ANSWERS": ast.List,
                    "NAME": str,
                    "PLEDGE": str
                    }

        for var in types:
            self.assertIn(var, [a.targets[0].id for a in assigns], "You "
                    "should only define the variables listed in the "
                    "description: {}. {} is missing from your solution.".format(list(types), var))

        for assign in assigns:
            self.assertEqual(len(assign.targets), 1, "You should assign to one"
                    " variable at a time.")
            variable = assign.targets[0].id
            self.assertIn(variable, types, "Either you defined a variable that"
                    " was not listed in the description, or you have a typo. "
                    "Please check your variable names and try again.")

            msg = "You did not assign the correct value to the {} variable. " \
                    "Check the instructions and try again.".format(variable)
            if sys.version_info >= (3, 8) and isinstance(assign.value, ast.Constant):
                self.assertIs(type(assign.value.value), types[variable], msg)
            else:
                self.assertIs(type(assign.value), types[variable], msg)

            if variable == "ANSWERS":
                list_elts = assign.value.elts
                self.assertGreaterEqual(len(list_elts), 16, "You need at least"
                        " 16 survey responses recorded in your list variable.")
                if any([not isinstance(elt, ast.Num) for elt in list_elts]):
                    self.fail("All of your survey responses should be numbers.")
            elif variable == "PLEDGE":
                self.assertEqual(assign.value.s.replace('\n', ' ').strip(), "I swear that I actually "
                        "asked this question of at least 16 people and "
                        "recorded their data without modifying the results. I"
                        " understand that falsifying data in this course is an"
                        " academic honor code violation.")

if __name__ == "__main__":
    unittest.main()
