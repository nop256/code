import ast
import unittest
import unittest.mock

import asttest

class TestMutabilityWrongReturn(asttest.ASTTest):

    def setUp(self):
        super().setUp("mutability_wrong_return.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        func = self.match_signature("get_front_of_weekdays", 1)
        self.assertIsNotNone(func, "Do not change the name or parameter of the"
                " given function.")

        lists = self.find_all(ast.List)
        self.assertEqual(len(lists), 1, "You should only have one list literal"
                " in your program.")
        elts = lists[0].elts
        modify = "Do not modify the list given in the program."
        self.assertEqual(len(elts), 5, modify)
        self.assertTrue(all(isinstance(e, ast.Str) for e in elts), modify)
        self.assertEqual([s.s for s in elts],
                ["mon", "tues", "wed", "thurs", "fri"], modify)

        tests = [("monday", "mon"),
                ("friday", "fri"),
                ("thursday", "thurs"),
                ("saturday", "weekend"),
                ("sunday", "weekend")]
        for test in tests:
            with self.subTest(day=test[0]):
                from mutability_wrong_return import get_front_of_weekdays
                result = get_front_of_weekdays(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()
