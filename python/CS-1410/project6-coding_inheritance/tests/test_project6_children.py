import ast
import unittest

import asttest
import child1, child2, child3, child4

class TestProject6_child(asttest.ASTTest):

    def setUp(self):
        pass

    def test_children_syntax(self):
        self.objects_with_attributes = 0
        super().setUp("child1.py")
        self.helper_required_child_syntax()
        super().setUp("child2.py")
        self.helper_required_child_syntax()
        super().setUp("child3.py")
        self.helper_required_child_syntax()
        super().setUp("child4.py")
        if len(self.file)>=1:
            self.helper_required_child_syntax()
        self.assertGreaterEqual(self.objects_with_attributes,1,f"{self.filename}: At least one of the children needs an attribute")


    def test_children_execution(self):
        super().setUp("child1.py")
        self.helper_correct_result()
        super().setUp("child2.py")
        self.helper_correct_result()
        super().setUp("child3.py")
        self.helper_correct_result()
        super().setUp("child4.py")
        if len(self.file)>=1:
            self.helper_correct_result()

    def find_all_methods(self, class_node):
        return self.find_all(ast.FunctionDef, class_node)

    def required_child_syntax_import_parent(self):
        # Get all imported files and objects and put in set
        imported_files = set()
        imported_objects = set()
        from_import = self.find_all(ast.ImportFrom)
        for imp in from_import:
            imported_files.add(imp.module)
            for nm in imp.names:
                imported_objects.add(nm.name)
        imports = self.find_all(ast.Import)
        for imp in imports:
            if isinstance(imp.names,list):
                for nm in imp.names:
                    if isinstance(nm,ast.alias):
                        imported_files.add(nm.name)
        self.assertTrue(len(imported_files)>=1,f"{self.filename}: Must import parent")
        #print(f"imported_files = {imported_files}")
        #print(f"imported_objects = {imported_objects}")
        return imported_files

    def required_child_syntax_one_class_in_file(self, imported_files):
        # Class definition tests - must have inheritance
        class_defs = self.find_all(ast.ClassDef)
        self.assertEqual(1,len(class_defs),f"{self.filename}: Need to define exactly 1 class in the file")
        class_def = class_defs[0]
        parent_object = None
        object_name = class_def.name
        if isinstance(class_def.bases,list):
            if class_def.bases:
                if isinstance(class_def.bases[0],ast.Name):
                    parent_object = class_def.bases[0].id
                elif isinstance(class_def.bases[0],ast.Attribute):
                    if isinstance(class_def.bases[0].value,ast.Name):
                        self.assertTrue(class_def.bases[0].value.id in imported_files, f"{self.filename}: line {class_def.lineno}: Need to import file")
                        parent_object = class_def.bases[0].attr
        self.assertTrue(parent_object,f"{self.filename}: line {class_def.lineno}: Must show inheritance")
        #print(f"object_name = {object_name}")
        #print(f"parent_object = {parent_object}")
        return class_def

    def required_child_syntax_class_docstring(self, class_def):
        """The class most have a docstring."""
        self.assertIsInstance(class_def.body[0],ast.Expr,f"{self.filename}: Need to have a docstring for your class")
        self.assertIsInstance(class_def.body[0].value,ast.Constant,f"{self.filename}: Need to have a docstring for your class")
        return

    def required_child_syntax_init_first_method(self, class_def, function_defs):
        """__init__ must be the first method of the class."""
        self.assertGreaterEqual(len(function_defs), 1, f"{self.filename}: {class_def.name}: Must have at least one method.")
        if len(function_defs) >= 1:
            self.assertEqual(function_defs[0].name,"__init__",f"{self.filename}: {class_def.name}: The first method should be the constructor")
        return

    def required_child_syntax_init_parameters(self, class_def, function_defs):
        self.assertTrue(len(function_defs[0].args.args) >= 1, f"{self.filename}: Must have at least 1 parameter in the constructor")
        return

    def required_child_syntax_init_datamembers_use_self(self, class_def, function_defs):
        constructor_assigns = self.find_all(ast.Assign,function_defs[0])
        if constructor_assigns:
            self.objects_with_attributes += 1
            attributes = set()
            for assign in constructor_assigns:
                if isinstance(assign.targets[0],ast.Attribute) and assign.targets[0].value.id=='self':
                    attributes.add(assign.targets[0].attr)
            #print(f"attributes = {attributes}")
            self.assertTrue(len(attributes)>=1,f"{self.filename}: Data Members must begin with self.")
        return

    def required_child_syntax_init_constructor_chaining(self, class_def, function_defs):
        constructor_calls = self.find_all(ast.Call,function_defs[0])
        super_call = False
        if constructor_calls:
            for call in constructor_calls:
                if isinstance(call.func,ast.Attribute):
                    if isinstance(call.func.value,ast.Call):
                        if isinstance(call.func.value.func,ast.Name):
                            if call.func.value.func.id == "super" and call.func.attr=="__init__":
                                super_call = True
        self.assertTrue(super_call,f"{self.filename}: Must use constructor chaining to call the parent's constructor")
        return

    def helper_required_child_syntax(self):
        #print(self.debug_tree())
        imported_files = self.required_child_syntax_import_parent()
        class_def = self.required_child_syntax_one_class_in_file(imported_files)
        self.required_child_syntax_class_docstring(class_def)
        function_defs = self.find_all_methods(class_def)
        self.required_child_syntax_init_first_method(class_def, function_defs)
        self.required_child_syntax_init_parameters(class_def, function_defs)
        self.required_child_syntax_init_datamembers_use_self(class_def, function_defs)
        self.required_child_syntax_init_constructor_chaining(class_def, function_defs)


        #test to_string methods
        to_string_func = None
        for func in function_defs:
            if func.name == "to_string":
                to_string_func = func
        self.assertTrue(to_string_func,f"{self.filename}: Must have to_string method")
        to_string_calls = self.find_all(ast.Call,to_string_func)
        super_call = False
        if to_string_calls:
            for call in to_string_calls:
                if isinstance(call.func,ast.Attribute):
                    if isinstance(call.func.value,ast.Call):
                        if isinstance(call.func.value.func,ast.Name):
                            if call.func.value.func.id == "super" and call.func.attr=="to_string":
                                super_call = True
        self.assertTrue(super_call,f"{self.filename}: Must use constructor chaining to call the parent's to_string method")

        #general method tests
        func_set = set()
        for func in function_defs:
            func_set.add(func.name)
            self.assertTrue(len(func.args.args)>=1,f"{self.filename}: self should be a parameter in all methods")
            self.assertEqual(func.args.args[0].arg,'self',f"{self.filename}: First parameter should be self")
            self.assertIsInstance(func.body[0],ast.Expr,f"{self.filename}: Need to have a docstring for each method")
            self.assertIsInstance(func.body[0].value,ast.Constant,f"{self.filename}: Need to have a docstring for each method")

        #restrict input and output in class object
        calls = self.find_all(ast.Call,class_def)
        for call in calls:
            if isinstance(call.func,ast.Name):
                self.assertNotEqual(call.func.id,"print",f"{self.filename}: line {call.lineno}: Must not use the print function in the class")
                self.assertNotEqual(call.func.id,"input",f"{self.filename}: line {call.lineno}: Must not use the input function in the class")

        #check tests in file
        test_node = None
        for node in self.tree.body:
            if isinstance(node, ast.If) and \
            isinstance(node.test,ast.Compare) and \
            isinstance(node.test.left,ast.Name) and \
            node.test.left.id=="__name__" and \
            isinstance(node.test.comparators[0],ast.Constant) and \
            node.test.comparators[0].value=="__main__":
                test_node = node
        self.assertIsNotNone(test_node,f"{self.filename}: Must include code to test the class. Remember 'if __name__==\"__main__\":'")
        #assigned an object
        all_functions=self.find_all(ast.FunctionDef)
        for f in all_functions:
            if f.name == "main":
                test_node = f
        test_node_assigns = self.find_all(ast.Assign,test_node)
        created_and_stored_object = False

        #check if objects are instantiated
        for tn_assign in test_node_assigns:
            if isinstance(tn_assign.value,ast.Call) and isinstance(tn_assign.value.func,ast.Name) and (tn_assign.value.func.id == class_def.name):
                created_and_stored_object = True
        self.assertTrue(created_and_stored_object,f"{self.filename}: Must instantiate and store a class object")

        #end of check of instantiated objects
        test_calls = self.find_all(ast.Call,test_node)
        test_assigns = self.find_all(ast.Assign,test_node)
        myobj_assign_set = set()
        object_created = False
        for test_assign in test_assigns:
            if isinstance(test_assign.targets,list):
                if isinstance(test_assign.targets[0],ast.Name):
                    if isinstance(test_assign.value,ast.Call):
                        if isinstance(test_assign.value.func,ast.Name):
                            myobj_assign_set.add(test_assign.targets[0].id)
                            if test_assign.value.func.id == class_def.name:
                                object_created = True
        self.assertTrue(object_created,f"{self.filename}: Must create an object to test it")
        #print(f"myobject assign set: {myobj_assign_set}")
        #print(f"Function set: {func_set}")
        test_call_set = set(["__init__"])
        for call in test_calls:
            if isinstance(call.func,ast.Attribute):
                if isinstance(call.func.value,ast.Name):
                    if call.func.value.id in myobj_assign_set:
                        test_call_set.add(call.func.attr)
        #print(f"Test Call set: {test_call_set}")
        self.assertTrue(func_set.issubset(test_call_set), f"{self.filename}: Must call all methods.")

    def helper_correct_result(self):
        namespace = {"__name__": "__main__","print":self.print_replacement}
        exec(self.file,namespace)
        self.assertTrue(len(self.printed_lines)>=2, f"{self.filename}: You should print (using to_string) after every method call")


if __name__ == "__main__":
    unittest.main()
