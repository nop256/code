import ast
import unittest

import asttest

class TestMutabilityAppendingStrings(asttest.ASTTest):

    def setUp(self):
        super().setUp("mutability_appending_strings.py")

    def test_required_syntax(self):
        changed = "Do not delete the values from the assignment statements."
        hint = "Simply change the assignment statements so that the " \
                ".append() method works as intended."

        lists = self.find_all(ast.List)
        self.assertGreaterEqual(len(lists), 1, changed)
        self.assertEqual(len(lists), 1, "Do not add any list literals. "+hint)
        self.assertEqual([], lists[0].elts, changed)
        strs = self.find_all(ast.Str)
        for str_ in ["Dogs", "Cups", "Cards", "Petals"]:
            self.assertIn(str_, [s.s for s in strs], changed)

        self.assertEqual(len(self.find_all(ast.Add)), 0, "Do not use the add "
                "operator. " + hint)
        self.assertEqual(len(self.find_function_calls("list")), 0, "Do not "
                "create a new list. " + hint)

        self.assertIn("things", [name.id for name in self.find_all(ast.Name)],
                "Don't delete the variable named things. You just need to make"
                " sure it doesn't end up with the value None!")

        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print a "
                "single line.")
        self.assertEqual(self.printed_lines[0], ["Dogs", "Cups", "Cards", "Petals"],
            "You are not printing the correct result.")


if __name__ == "__main__":
    unittest.main()
