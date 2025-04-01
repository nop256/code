import ast
import sys
import asttest
from unittest import mock

class TestKaleidoscope(asttest.ASTTest):

    def setUp(self):
        sys.modules['turtle'] = mock.Mock()
        super().setUp("kaleidoscope.py")

    def test_functions(self):
        func_defs = self.find_all(ast.FunctionDef)
        self.assertGreaterEqual(len(func_defs), 8, "You should have a minimum "
                "of 8 functions.")

        turtles = set()
        for func_def in func_defs:
            calls = self.find_all(ast.Call, func_def)
            for call in calls:
                if isinstance(call.func, ast.Attribute):
                    if call.func.value.id == "turtle" and call.func.attr == "Turtle":
                        turtles.add(func_def.name)
                        break
        self.assertGreaterEqual(len(turtles), 4, "You should have a minimum of 4 "
                "turtle objects")

        modifiers = set()
        for func_def in func_defs:
            calls = self.find_all(ast.Call, func_def)
            for call in calls:
                if isinstance(call.func, ast.Attribute):
                    if call.func.attr in ["right", "left", "forward", "fd", "rt", "stamp"]:
                        modifiers.add(func_def.name)
                        break
        #self.assertGreaterEqual(len(modifiers), 3, "You should have a minimum "
                #"of 3 functions that move/change your turtle objects.")

        # main
        called_range = False
        called_randrange = False
        for func_def in func_defs:
            if func_def.name == "main":
                calls = self.find_all(ast.Call, func_def)
                for call in calls:
                    if isinstance(call.func, ast.Name):
                        name = call.func.id
                        if name in turtles:
                            turtles.remove(name)
                        elif name in modifiers:
                            modifiers.remove(name)
                        elif name == "range":
                            called_range = True
                    elif isinstance(call.func, ast.Attribute):
                        if call.func.attr == "randrange":
                            called_randrange = True


        self.assertTrue(called_range, "You should call the range() function "
                "in your main function to loop over your turtle objects")
        self.assertTrue(called_randrange, "You should call the randrange() "
                "function in your main function to make the designs randomly "
                "generated.")
        self.assertEqual(len(turtles), 0, "You should call all of your "
                "functions that create turtle objects. Missing function "
                f"calls: {turtles}.")
        self.assertEqual(len(modifiers), 0, "You should call all of your "
                "functions that move/change the turtle objects. Missing "
                f"function calls: {modifiers}.")
