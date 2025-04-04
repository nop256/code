import ast
import unittest

import asttest

startover = "I recommend replacing your file with the one found in the " \
        "starter folder to start over and try again."

class TestIfDrivenToRent(asttest.ASTTest):

    def setUp(self):
        super().setUp("if_driven_to_rent.py")

    def test_required_syntax(self):
        ifs = self.find_all(ast.If)
        binops = self.find_all(ast.Compare)
        prints = self.find_function_calls("print")
        assign_values = {assign.targets[0].id:assign.value for assign in self.find_all(ast.Assign)}
        self.assertEqual(len(ifs), 3, "Do not add or remove if statements. "
                + startover)
        self.assertEqual(len(binops), 2, "Do not modify the comparisons. "
                + startover)
        self.assertEqual(len(prints), 4, "Do not add or remove any print "
                "function calls. " + startover)
        if not (ifs[0].body[0] == ifs[1]) or not (ifs[1].body[0] == ifs[2]):
            self.fail("Do not modify the structure of the if statements. "
                    + startover)
        if 'age' not in assign_values and not isinstance(assign_values['age'], int):
            self.fail("You will need to initalize a variable called "
                    "age with an integer as its value.")
        if 'has_license' not in assign_values and not isinstance(assign_values['has_license'], int):
            self.fail("You will need to initalize a variable called "
                    "has_license with an integer as its value.")

        age = assign_values['age'].n
        has_license = assign_values['has_license'].value
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly"
                " one line.")
        out = self.printed_lines[0]
        if "Too old" in self.printed_lines and age < 1000:
            self.fail("Your output does not make sense for the age listed (too young).")
        elif "Too young" in self.printed_lines and age >= 21:
            self.fail("Your output does not make sense for the age listed (too old).")
        elif "Doesn't have a license" in self.printed_lines and has_license:
            self.fail("Your output does not make sense; you say you do have a license!")
        elif "Can rent a car" in self.printed_lines and (not has_license or not (21 <= age < 1000)):
            self.fail("Your output doesn't make sense for that <code>age</code> and <code>has_license</code>.")

        if out not in ("Too old", "Too young", "Doesn't have a license", "Can rent a car"):
            self.fail("You are printing the wrong thing! '{}' is not a valid "
                    "output message.".format(out))

if __name__ == "__main__":
    unittest.main()
