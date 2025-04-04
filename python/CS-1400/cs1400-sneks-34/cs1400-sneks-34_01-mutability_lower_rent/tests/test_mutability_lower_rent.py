import ast
import unittest

import asttest

class TestMutabilityLowerRent(asttest.ASTTest):

    def setUp(self):
        super().setUp("mutability_lower_rent.py")

    def test_required_syntax(self):
        modified = "Do not modify the string literal. Leave it as all caps " \
                "and use the .lower() method to properly change the value."

        message = "THE RENT IS TOO HIGH!"
        self.assertNotIn(message.lower(), self.file, modified)
        self.assertIn(message, self.file, modified)

        assigns = self.find_all(ast.Assign)
        found = False
        for assign in assigns:
            target = assign.targets[0]
            if (isinstance(target, ast.Name) and
                    target.id == "message"):
                found = True
                self.assertEqual(assign.value.s, message, modified)
                break
        self.assertTrue(found, "Do not remove the message variable.")

        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You are not printing the"
                " correct result.")
        self.assertNotEqual(self.printed_lines[0], message, "You have not made"
                " the variable's value lowercase; it is still all caps.")
        self.assertEqual(self.printed_lines[0], message.lower(), "You are not "
                "printing the correct result.")

if __name__ == "__main__":
    unittest.main()
