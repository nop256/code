import ast
import unittest
import unittest.mock

import asttest

class TestScopeCallingInside(asttest.ASTTest):

    def setUp(self):
        super().setUp("scope_calling_inside.py")

    def test_required_syntax(self):
        msg = "You should not change the improve_message function."
        improve_func = self.match_signature("improve_message", 1)
        self.assertIsNotNone(improve_func, msg)
        returns = self.find_all(ast.Return, improve_func)
        self.assertEqual(len(returns), 1, msg)
        self.assertIsInstance(returns[0].value, ast.Call, msg)
        self.assertIsInstance(returns[0].value.func, ast.Attribute, msg)
        self.assertIsInstance(returns[0].value.func.value, ast.Name, msg)
        self.assertEqual(returns[0].value.func.value.id, 'a_string', msg)
        self.assertEqual(returns[0].value.func.attr, 'replace', msg)
        self.assertEqual(len(returns[0].value.args), 2, msg)
        self.assertIsInstance(returns[0].value.args[0], ast.Str, msg)
        self.assertIsInstance(returns[0].value.args[1], ast.Str, msg)
        self.assertEqual(returns[0].value.args[0].s, 'dog', msg)
        self.assertEqual(returns[0].value.args[1].s, 'doggo', msg)

        combine_func = self.match_signature("combine_messages", 3)
        self.assertIsNotNone(improve_func, "You should not change the "
                "name or parameters of the combine_messages function.")
        returns = self.find_all(ast.Return, combine_func)
        self.assertEqual(len(returns), 1, "Do not add any return statements to"
                " the combine_messages function. Neither should you remove the"
                " one that is already there. Instead, you should change the "
                "return statement to properly improve the message.")

        method_names = self.get_method_calls(combine_func)
        self.assertEqual(len(method_names), 0, "You should not call any method"
                " functions in the combine_messages function (that includes "
                ".replace()).")
        self.assertNotIn("replace", method_names, "You should not call the "
                "replace method function in the combine_messages function. "
                "Instead, what function do you have available to you in your "
                "program to specifically replace instances of the string 'dog'"
                " with 'doggo'.")

        call_names = self.get_function_calls(combine_func)
        self.assertGreaterEqual(len(call_names), 1, "You should call the "
                "improve_message function in the combine_messages function.")
        self.assertEqual(len(call_names), 1, "You should only call one "
                "function in the combine_messages function. While it does work"
                " to call the improve_message for each string, is it a good "
                "idea? Think about how the improve_message (specifically, "
                ".replace()) works. We actually only need to call the improve "
                "message one time to work as intended which is a much cleaner "
                "approach.")

    def test_correct_result_combine_messages(self):
        tests = [("a", "b", "c", "a\nb\nc"),
                 ("", "", "", "\n\n"),
                 ("dog", "dog", "dog", "doggo\ndoggo\ndoggo"),
                 ("the", "dog", "is good", "the\ndoggo\nis good")]
        for test in tests:
            with unittest.mock.patch('sys.stdout') as buffer:
                with self.subTest(first=test[0], second=test[1], third=test[2]):
                    from scope_calling_inside import combine_messages
                    result = combine_messages(test[0], test[1], test[2])
                    self.assertEqual(result, test[3], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned\n'{}'\n however, it should have returned "
                            "\n'{}'".format(test[0:3], result, test[3]))

    def test_correct_result_improve_message(self):
        tests = [("dog", "doggo"),
                 ("cat", "cat"),
                 ("", ""),
                 ("The doggo", "The doggogo")]
        for test in tests:
            with unittest.mock.patch('sys.stdout') as buffer:
                with self.subTest(a_string=test[0]):
                    from scope_calling_inside import improve_message
                    result = improve_message(test[0])
                    self.assertEqual(result, test[1], "Do not change the "
                            "improve_message function! When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()
