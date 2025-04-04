import ast
import unittest
import unittest.mock

import asttest

class TestFilesFileSize(asttest.ASTTest):

    def setUp(self):
        super().setUp("files_file_size.py")

    def test_required_syntax(self):
        self.assertNotEqual(len(self.find_function_calls("open")), 0, "You "
                "need to *open* the file.")
        self.assertNotEqual(len(self.find_method_calls("close")), 0, "Don't "
                "forget to close the file!")

        self.assertEqual(len(self.find_function_calls("len")), 0, "You may "
                "not use the built-in len function.")
        self.assertEqual(len(self.find_all(ast.ListComp)), 0, "List "
                "comprehensions are not the best way to solve this question, "
                "because we need print as we loop.")
        self.assertEqual(len(self.find_all(ast.List)), 0, "You should not be "
                "creating a new list.")
        self.assertEqual(len(self.find_method_calls("read")), 0, "You may not "
                "use the built-in read method.")
        self.assertEqual(len(self.find_method_calls("readlines")), 0, "You may"
                " not use the built-in readlines method.")
        self.assertEqual(len(self.find_method_calls("split")), 0,
                "You should not need to call the split method.")
        self.assertEqual(len(self.find_method_calls("strip")), 0,
                "You should not need to call the strip method.")
        self.assertEqual(len(self.find_method_calls("rstrip")), 0,
                "You should not need to call the rstrip method.")

        func = self.match_signature('calculate_file_size', 1)
        tests = [('rainfall.txt', 28830),
                ('names.txt', 119),
                ('empty.txt', 0)]

        with unittest.mock.patch("sys.stdout") as mock_stdout:
            for test in tests:
                with self.subTest(a_number=test[0]):
                    from files_file_size import calculate_file_size
                    result = calculate_file_size(test[0])
                    self.assertEqual(result, test[1], "Your function is "
                            "not returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned '{}'."
                            .format(test[0], result, test[1]))

            self.ensure_coverage(["calculate_file_size"], .5)
            self.assertGreaterEqual(len(self.find_function_calls("assert_equal")),
                    3, "You should write at least three unit tests.")

if __name__ == "__main__":
    unittest.main()
