import ast
import unittest

import asttest

class TestLoopPatternsMissingIter(asttest.ASTTest):

    def setUp(self):
        super().setUp("loop_patterns_missing_iter.py")

    def test_required_syntax(self):
        fors = self.find_all(ast.For)
        self.assertEqual(len(fors), 1, "You should use a single for loop.")

        sums = self.find_function_calls("sum")
        self.assertEqual(len(sums), 0, "You cannot use the sum function for "
                "this problem. You need to demonstrate that you know how to "
                "sum values using a for loop.")

        self.assert_sum_list()
        self.assert_zero_initialization()
        self.assert_target_used()
        self.assert_not_counting()

    def test_correct_result(self):
        self.exec_solution()
        self.assertIn(sum([223, 251, 317, 636]), self.printed_lines, "You are "
                "not printing the right result.")

    def assert_zero_initialization(self):
        """ins_cont.missing_zero_initialization()"""
        fors = self.find_all(ast.For)
        accumulator = None
        loop_acu = None
        for loop in fors:
            assignments = self.find_all(ast.Assign, loop)
            for assignment in assignments:
                binops = self.find_all(ast.BinOp, assignment)
                if len(binops) > 0:
                    lhs = assignment.targets[0]
                    for binop in binops:
                        names = [name.id for name in self.find_all(ast.Name, binop)]
                        if lhs.id in names and isinstance(binop.op, ast.Add):
                            accumulator = lhs
                            loop_acu = loop
        accu_init = False
        if accumulator is not None:
            assignments = self.find_all(ast.Assign)
            for assignment in assignments:
                if loop_acu.lineno > assignment.lineno:
                    lhs = assignment.targets[0]
                    if (lhs.id == accumulator.id and
                            isinstance(assignment.value, ast.Num) and
                            assignment.value.n == 0):
                        accu_init = True
                        break
        if not accu_init and accumulator is not None:
            self.fail("The addition on the first iteration step is not correct"
                    " because either the variable {0!s} has not been "
                    "initialized to an appropriate initial value or it has not"
                    " been placed in an appropriate location."
                    .format(accumulator.id))

    def assert_sum_list(self):
        """ins_cont.wrong_cannot_sum_list()"""
        fors = self.find_all(ast.For)
        for loop in fors:
            list_prop = loop.iter # ast.Name
            assignments = self.find_all(ast.Assign, loop)
            for assignment in assignments:
                binops = self.find_all(ast.BinOp, assignment)
                for binop in binops:
                    names = [name.id for name in self.find_all(ast.Name, binop)]
                    if list_prop.id in names and isinstance(binop.op, ast.Add):
                        self.fail("Addition can only be done with a single "
                                "value at a time, not with an entire list at "
                                "one time.")

    def assert_target_used(self):
        """ins_cont.wrong_names_not_agree_8_4()"""
        fors = self.find_all(ast.For)
        for loop in fors:
            list_prop = loop.target # ast.Name
            names = [name for name in self.find_all(ast.Name, loop) if name.id == list_prop.id]
            self.assertGreaterEqual(len(names), 2, "You did not use the "
                    "iteration variable in the body of the for loop.")

    def assert_not_counting(self):
        """ins_cont.wrong_should_be_summing()"""
        fors = self.find_all(ast.For)
        for loop in fors:
            assignments = self.find_all(ast.Assign, loop)
            for assignment in assignments:
                binops = self.find_all(ast.BinOp, assignment)
                for binop in binops:
                    if (isinstance(binop.op, ast.Add) and
                        ((isinstance(binop.left, ast.Num)
                                and binop.left.n == 1)
                            or (isinstance(binop.right, ast.Num)
                                and binop.right.n == 1))):
                        self.fail("This problem asks for the total of all the "
                                "values in the list not the number of items in"
                                " the list.")

if __name__ == "__main__":
    unittest.main()
