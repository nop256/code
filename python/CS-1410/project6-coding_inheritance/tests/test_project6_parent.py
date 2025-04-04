import ast
import unittest

import asttest

class TestProject6_Parent(asttest.ASTTest):

    def setUp(self):
        super().setUp("parent.py")
        return

    def find_all_methods(self, class_node):
        return self.find_all(ast.FunctionDef, class_node)

    def required_syntax_one_class_in_file(self):
        """There must be one class defined in the module."""
        class_defs = self.find_all(ast.ClassDef)
        self.assertEqual(1,len(class_defs),f"{self.filename}: Need to define exactly 1 class in the file")
        return class_defs

    def required_syntax_class_docstring(self, class_def):
        """The class most have a docstring."""
        self.assertIsInstance(class_def.body[0],ast.Expr,f"{self.filename}: Need to have a docstring for your class")
        self.assertIsInstance(class_def.body[0].value,ast.Constant,f"{self.filename}: Need to have a docstring for your class")
        return

    def required_syntax_init_first_method(self, class_def, function_defs):
        """__init__ must be the first method of the class."""
        self.assertGreaterEqual(len(function_defs), 1, f"{self.filename}: {class_def.name}: Must have at least one method.")
        if len(function_defs) >= 1:
            self.assertEqual(function_defs[0].name,"__init__",f"{self.filename}: {class_def.name}: The first method should be the constructor")
        return

    def required_syntax_init_sets_datamembers(self, class_def, function_defs):
        """__init__ must assign into data members."""
        # assignments in the constructor
        constructor_assigns = self.find_all(ast.Assign,function_defs[0])
        self.assertTrue(len(constructor_assigns)>=1,f"{self.filename}: {class_def.name}: Must have at least 1 data member assigned to in the constructor.")

        # collect all "self.attribute = " attributes
        attributes = set()
        for assign in constructor_assigns:
            if isinstance(assign.targets[0],ast.Attribute) and assign.targets[0].value.id=='self':
                attributes.add(assign.targets[0].attr)
        self.assertTrue(len(attributes)>=1,f"{self.filename}: {class_def.name}.__init__: Data Members must begin with self.")
        return

    def required_syntax_to_string_must_exist(self, class_def, function_defs):
        """to_string() method must exist."""
        found_to_string = False
        func_set = set()
        for func in function_defs:
            func_set.add(func.name)
            if func.name=="to_string":
                found_to_string = True
        self.assertTrue(found_to_string,f"{self.filename}: {class_def.name}: You must have a to_string method.")
        return func_set

    def required_syntax_methods_have_self_parameter(self, class_def, function_defs):
        """all methods must have the self parameter, as the first parameter."""
        for func in function_defs:
            self.assertTrue(len(func.args.args)>=1,f"{self.filename}: {class_def.name}: {func.name}: self should be a parameter in all methods.")
            self.assertEqual(func.args.args[0].arg,'self',f"{self.filename}: {class_def.name}: {func.name}: First parameter should be self.")
        return

    def required_syntax_methods_have_docstring(self, class_def, function_defs):
        """all methods must a docstring."""
        for func in function_defs:
            self.assertIsInstance(func.body[0],ast.Expr,f"{self.filename}: {class_def.name}: {func.name}: Need to have a docstring for each method.")
            self.assertIsInstance(func.body[0].value,ast.Constant,f"{self.filename}: {class_def.name}: {func.name}: Need to have a docstring for each method.")
        return

    def required_syntax_many_methods(self, class_def, function_defs):
        """Must have at least 3 methods total."""
        self.assertTrue(len(function_defs)>=3,f"{self.filename}: {class_def.name}: Need to have at least 1 method besides constructor and to_string.")
        return

    def required_syntax_methods_have_flow_control(self, class_def, function_defs):
        """Must have at least 2 If statements in the methods."""
        self.assertTrue(len(self.find_all(ast.If,class_def))>=2,f"{self.filename}: {class_def.name}: Methods are not complex enough. Need more conditional logic.")
        return

    def required_syntax_methods_do_not_call_print(self, class_def, function_defs):
        """Methods must not call print."""
        calls = self.find_all(ast.Call,class_def)
        for call in calls:
            if isinstance(call.func,ast.Name):
                self.assertNotEqual(call.func.id,"print",f"{self.filename}: {class_def.name}: line {call.lineno}: Must not use the print function in the class")
        return

    def required_syntax_methods_if_name_equals_main(self, class_def, function_defs):
        """Must have if __name__ == "__main__":"""
        test_node = None
        for node in self.tree.body:
            if isinstance(node, ast.If) and \
            isinstance(node.test,ast.Compare) and \
            isinstance(node.test.left,ast.Name) and \
            node.test.left.id=="__name__" and \
            isinstance(node.test.comparators[0],ast.Constant) and \
            node.test.comparators[0].value=="__main__":
                test_node = node

        self.assertIsNotNone(test_node,f"{self.filename}: {class_def.name}: Must include code to test the class. Remember 'if __name__==\"__main__\":'")

        #assigned an object
        all_functions=self.find_all(ast.FunctionDef)
        for f in all_functions:
            if f.name == "main":
                test_node = f
        return test_node

    def required_syntax_test_creates_object(self, class_def, test_node):
        """Create an object in the test code."""
        test_node_assigns = self.find_all(ast.Assign,test_node)
        created_and_stored_object = False
        for tn_assign in test_node_assigns:
            if isinstance(tn_assign.value,ast.Call) and isinstance(tn_assign.value.func,ast.Name) and (tn_assign.value.func.id == class_def.name):
                created_and_stored_object = True
        self.assertTrue(created_and_stored_object,f"{self.filename}: {class_def.name}: Must instantiate a class object in test code.")
        return

    def required_syntax_test_calls_all_methods(self, class_def, test_node, func_set):
        """Call all methods in the test code."""
        test_calls = self.find_all(ast.Call,test_node)
        test_call_set = set(["__init__"])
        for call in test_calls:
            if isinstance(call.func,ast.Attribute):
                test_call_set.add(call.func.attr)
        self.assertEqual(test_call_set, func_set,f"{self.filename}: {class_def.name}: Must call all methods.")
        self.assertTrue(len(test_call_set)==len(func_set),f"{self.filename}: {class_def.name}: Must call all methods.")

        return


    def test_required_syntax(self):

        #print(self.debug_tree())

        ###########################################################
        # - exactly one class must be defined in the file
        # - class docstring is required
        # - __init__ is required as the first method
        # - class must have at least 1 data member assigned in __init__
        # - to_string method must exist
        # - all methods must have self as the first parameter
        # - all methods must have a docstring
        # - must have at least 3 methods
        # - must have flow control in class methods
        # - must not call print in any class method
        # - must have if __name__ == "__main__": test code
        # - must create an object
        # - must call all methods
        #
        class_defs = self.required_syntax_one_class_in_file()
        class_def = class_defs[0]
        self.required_syntax_class_docstring(class_def)
        function_defs = self.find_all_methods(class_def)
        self.required_syntax_init_first_method(class_def, function_defs)
        self.required_syntax_init_sets_datamembers(class_def, function_defs)
        func_set = self.required_syntax_to_string_must_exist(class_def, function_defs)
        self.required_syntax_methods_have_self_parameter(class_def, function_defs)
        self.required_syntax_methods_have_docstring(class_def, function_defs)
        self.required_syntax_many_methods(class_def, function_defs)
        self.required_syntax_methods_have_flow_control(class_def, function_defs)
        self.required_syntax_methods_do_not_call_print(class_def, function_defs)
        test_node = self.required_syntax_methods_if_name_equals_main(class_def, function_defs)
        self.required_syntax_test_creates_object(class_def, test_node)
        self.required_syntax_test_calls_all_methods(class_def, test_node, func_set)
        return

    def test_correct_result(self):
        namespace = {"__name__": "__main__","print":self.print_replacement}
        exec(self.file,namespace)
        self.assertTrue(len(self.printed_lines)>=3, f"{self.filename}: You should print (using to_string) after every method call in the test code.")

if __name__ == "__main__":
    unittest.main()
