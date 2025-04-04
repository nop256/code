import ast
import unittest

import asttest


class TestProject6_main(asttest.ASTTest):

    def setUp(self):
        super().setUp("main.py")

    def test_required_syntax(self):
        #print(self.debug_tree())
        # Get all imported files and objects and put in set
        imported_files = set()
        imported_objects = set()
        from_import = self.find_all(ast.ImportFrom)
        for imp in from_import:
            imported_files.add(imp.module)
            for nm in  imp.names:
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
        self.assertGreaterEqual(len(imported_files),3,f"{self.filename}: Make sure to import all the child files")


        assigns = self.find_all(ast.Assign)
        created_and_stored_objects = set()
        created_list = None
        for assign in assigns:
            if isinstance(assign.value,ast.List) and isinstance(assign.targets,list) and isinstance(assign.targets[0],ast.Name):
                created_list = assign.targets[0].id
            if isinstance(assign.value,ast.Call):
                if isinstance(assign.value.func,ast.Name):
                    created_and_stored_objects.add(assign.value.func.id)
                    #print(f"created_and_stored_objects = {created_and_stored_objects}")
                elif isinstance(assign.value.func,ast.Attribute) and isinstance(assign.value.func.value,ast.Name):
                    created_and_stored_objects.add(assign.value.func.attr)
                    #print(f"created_and_stored_objects = {created_and_stored_objects}")
        self.assertTrue(created_list,f"{self.filename}: Must create a list")
        self.assertGreaterEqual(len(created_and_stored_objects),3,f"{self.filename}: Must instantiate and store all children objects")

        calls = self.find_all(ast.Call)
        to_string_count = 0
        append_count = 0
        for call in calls:
            if isinstance(call.func,ast.Attribute):
                if call.func.attr=="to_string":
                    to_string_count += 1
                if call.func.attr == "append":
                    append_count += 1
        self.assertEqual(to_string_count,1,f"{self.filename}: Should only call to_string in one place in main.py (inside a for-loop)")
        self.assertGreaterEqual(append_count,3,f"{self.filename}: Must append child objects to the list.")

    def test_correct_result(self):
        namespace = {"__name__": "__main__","print":self.print_replacement}
        exec(self.file,namespace)
        self.assertTrue(len(self.printed_lines)>=3, f"{self.filename}: You should print (using to_string) for every object")

if __name__ == "__main__":
    unittest.main()
