import ast
import unittest

import asttest

class TestModulesTheChoice(asttest.ASTTest):

    def setUp(self):
        super().setUp("modules_the_choice.py")

    def test_required_syntax(self):
        imports = self.find_all(ast.Import)
        froms = self.find_all(ast.ImportFrom)
        self.assertNotEqual(len(imports + froms), 0,
                "You need to import the random module!")
        found = False
        if imports:
            if not any(alias.name == 'random' for i in imports for alias in i.names):
                self.fail("You need to import the random module.")
            else:
                found = True
        if froms:
            if not found and not any(i.module == 'random' for i in froms):
                self.fail("You need to import the random module.")

        self.assertNotEqual(len(self.find_function_calls("print")), 0,
                "You need to print.")
        choice = (self.find_function_calls("choice") +
                self.find_method_calls("choice"))
        self.assertNotEqual(len(choice), 0,
                "You need to call the choice function.")

        list_vars = [to_list(l) for l in self.find_all(ast.List)]
        self.assertNotEqual(len(list_vars), 0, "You need to create a list of "
                "strings and store it in a variable.")
        self.assertEqual(len(list_vars), 1,
                "Just create a single list for this problem.")
        self.assertGreaterEqual(len(list_vars[0]), 4,
            "You need to have at least four restaurants in your string list.")
        self.assertTrue(all(isinstance(s, str) for s in list_vars[0]),
            "You should only add string values to your list.")

        self.exec_solution()
        if not any(r in self.printed_lines for r in list_vars[0]):
            self.fail("You should make sure your program prints one of the "
                    "values from your list.")
        self.assertEqual(len(self.find_all(ast.Subscript)), 0,
                "Do not use subscripting in this problem.")
        if self.find_all(ast.For) or self.find_all(ast.comprehension):
            self.fail("Do not use any loops to solve this problem.")

        original_output = self.printed_lines[:]
        success = False
        for i in range(10):
            self.printed_lines = []
            self.exec_solution()
            if original_output != self.printed_lines:
                success = True
        self.assertTrue(success, "I tried running your program 10 times, but "
                "it seems like each time it printed the same restaurant. Are "
                "you sure you used the choice function on your list?")

def to_list(lst):
    l = []
    for elt in lst.elts:
        l.append(get_value(elt))
    return l

def get_value(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Str):
        return node.s
    elif isinstance(node, ast.NameConstant):
        return node.value
    elif isinstance(node, ast.List):
        return to_list(node)
    elif isinstance(node, ast.Dict):
        return to_dict(node)
    return None

if __name__ == "__main__":
    unittest.main()
