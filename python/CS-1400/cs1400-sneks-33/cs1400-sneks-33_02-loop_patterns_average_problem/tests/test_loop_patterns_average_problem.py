import ast
import unittest
import unittest.mock

import asttest

class TestLoopPatternsAverageProblem(asttest.ASTTest):

    def setUp(self):
        super().setUp("loop_patterns_average_problem.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        func = self.match_signature("average", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        sums = self.find_function_calls("sum")
        self.assertEqual(len(sums), 0, "You cannot use the sum function for "
                "this problem. You need to demonstrate that you know how to "
                "sum values using a for loop.")

        lens = self.find_function_calls("len")
        self.assertEqual(len(lens), 0, "You cannot use the len function for "
                "this problem. You need to demonstrate that you know how to "
                "count values using a for loop.")

        self.assert_zero_initialization()
        self.warning_average_in_iteration()
        self.wrong_average_denominator()
        self.wrong_average_numerator()
        self.assert_sum_list()

        self.missing_counting_list()
        self.missing_summing_list()

        from loop_patterns_average_problem import average
        test = [1,4,3]
        result = average(test)
        with self.subTest(a_list=test):
            self.assertNotEqual(result, 3, "Your function is "
                    "calculating the count instead of the average.")
            self.assertNotEqual(result, 8, "Your function is "
                    "calculating the sum instead of the average.")
            self.assertNotEqual(result, 3, "Your function is "
                    "calculating the last value instead of the average.")
            self.assertNotEqual(result, 4, "Your function is "
                    "calculating the highest value instead of the average.")
        self.assertNotIsInstance(result, int, "Your function is returning an "
                "integer instead of a float. Are you using integer division to"
                " calculate the average?")

        tests = [([1,2,3], 2.0),
                ([1], 1.0),
                ([4,4,4], 4.0),
                ([0], 0.0)]
        for test in tests:
            with self.subTest(a_list=test[0]):
                result = average(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                2, "You should unit test your function at least twice.")
        self.ensure_coverage(['average'], .9)

    def warning_average_in_iteration(self):
        # TODO: also check for AugAssign
        fors = self.find_all(ast.For)
        for loop in fors:
            assigns = self.find_all(ast.Assign, loop)
            for assign in assigns:
                if (isinstance(assign.value, ast.BinOp) and
                        isinstance(assign.value.op, ast.Div)):
                    divide = assign.value.op
                    _total_ = divide.left
                    _count_ = divide.right
                    _average_ = assign.targets[0]
                    if (_total_.id != _count_.id != _average_.id and
                            _total_.id != _average_.id):
                        self.fail("An average value is best computed after the"
                                "properties named <code>{0!s}</code>(total) "
                                "and <code>{1!s}</code> are completely known "
                                "rather than recomputing the average on each "
                                "iteration.".format(_total_.id, _count_.id))

    def wrong_average_denominator(self):
        """When dividing to compute the average, the denominator should be the
        variable that was used to count."""
        """ TODO
        matches = find_matches("for ___ in ___:\n"
                               "    __expr__\n"  # where expr contains _count_ = _count_ + 1
                               "__expr2__")  # where expr2 contains ___/_value_
        # where _value_.id != _count_.id
        if matches:
            for match in matches:
                __expr__ = match["__expr__"]
                __expr2__ = match["__expr2__"]
                # _value_ = match["_value_"][0]
                submatches = find_expr_sub_matches("_count_ = _count_ + 1", __expr__)
                submatches02 = find_expr_sub_matches("___/_value_", __expr2__)
                if submatches and submatches02:
                    for submatch in submatches:
                        for submatch02 in submatches02:
                            _count_ = submatch["_count_"][0]
                            _value_ = submatch02["_value_"][0]
                            if _count_.id != _value_.id:
                                explain('The average is not calculated correctly.<br><br><i>(avg_denom)<i></br>')
        """


    def wrong_average_numerator(self):
        """When dividing to compute the average, the numerator should be the
        variable that was used to sum."""
        """ TODO
        matches = find_matches("for _item_ in ___:\n"
                               "    __expr__\n"  # where expr contains _total_ = _total_ + 1
                               "__expr2__")  # where expr2 contains _value_/___
        if matches:
            for match in matches:
                __expr__ = match["__expr__"]
                __expr2__ = match["__expr2__"]
                _item_ = match["_item_"][0]
                submatches = find_expr_sub_matches("_total_ = _total_ + {}".format(_item_.id), __expr__)
                submatches02 = find_expr_sub_matches("_value_/___", __expr2__)
                if submatches and submatches02:
                    for submatch in submatches:
                        for submatch02 in submatches02:
                            _value_ = submatch02["_value_"][0]
                            _total_ = submatch["_total_"][0]
                            if _total_.id != _value_.id:
                                explain('The average is not calculated correctly.<br><br><i>(avg_numer)<i></br>')
                                return True
        return False
        """

    def assert_counting(self):
        """
        has_count = False
        for_loops = self.find_all('For')
        if len(for_loops) > 0:
            for loop in for_loops:
                assigns = loop.find_all('Assign')
                if len(assigns) < 1:
                    continue
                for assign in assigns:
                    binops = assign.find_all('BinOp')
                    if len(binops) < 1:
                        continue
                    lhs = assign.targets[0]
                    for binop in binops:
                        if binop.has(lhs) and binop.has(1) and binop.op == 'Add':
                            has_count = True
        if not has_count:
            explain('Count the total number of items in the list using iteration.<br><br><i>(miss_count_list)<i></br>')
        """

    def assert_zero_initialization(self):
        """ins_cont.missing_zero_initialization()"""
        fors = self.find_all(ast.For)
        accumulator = None
        loop_acu = None
        for loop in fors:
            assigns = self.find_all(ast.Assign, loop)
            for assign in assigns:
                binops = self.find_all(ast.BinOp, assign)
                if len(binops) > 0:
                    lhs = assign.targets[0]
                    for binop in binops:
                        names = [name.id for name in self.find_all(ast.Name, binop)]
                        if lhs.id in names and isinstance(binop.op, ast.Add):
                            accumulator = lhs
                            loop_acu = loop
        accu_init = False
        if accumulator is not None:
            assigns = self.find_all(ast.Assign)
            for assign in assigns:
                if loop_acu.lineno > assign.lineno:
                    lhs = assign.targets[0]
                    if (lhs.id == accumulator.id and
                            isinstance(assign.value, ast.Num) and
                            assign.value.n == 0):
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
            assigns = self.find_all(ast.Assign, loop)
            for assign in assigns:
                binops = self.find_all(ast.BinOp, assign)
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

    def missing_summing_list(self):
        has_total = False
        fors = self.find_all(ast.For)
        for loop in fors:
            iter_prop = loop.target
            assigns = self.find_all(ast.Assign, loop)
            if len(assigns) > 0:
                for assign in assigns:
                    lhs = assign.targets[0]
                    binops = self.find_all(ast.BinOp, assign)
                    for binop in binops:
                        names = [name.id for name in self.find_all(ast.Name, binop)]
                        if (lhs.id in names and iter_prop.id in names and
                                isinstance(binop.op, ast.Add)):
                            has_total = True
            else:
                assigns = self.find_all(ast.AugAssign, loop)
                for assign in assigns:
                    print(ast.dump(assign))
                    if (isinstance(assign.value, ast.Name) and
                            assign.value.id == iter_prop.id and
                            isinstance(assign.op, ast.Add)):
                        has_total = True
        self.assertTrue(has_total, "Sum the total of all list elements using "
                "iteration.")

    def missing_counting_list(self):
        has_count = False
        fors = self.find_all(ast.For)
        for loop in fors:
            assigns = self.find_all(ast.Assign, loop)
            if len(assigns) > 0:
                for assign in assigns:
                    lhs = assign.targets[0]
                    binops = self.find_all(ast.BinOp)
                    for binop in binops:
                        names = [name.id for name in self.find_all(ast.Name, binop)]
                        nums = [num.n for num in self.find_all(ast.Num, binop)]
                        if (lhs.id in names and 1 in nums and
                                isinstance(binop.op, ast.Add)):
                            has_count = True
            else:
                assigns = self.find_all(ast.AugAssign, loop)
                for assign in assigns:
                    if (isinstance(assign.value, ast.Num) and
                            assign.value.n == 1 and
                            isinstance(assign.op, ast.Add)):
                        has_count = True
        self.assertTrue(has_count, "Count the total number of items in the "
                "list using iteration.")

if __name__ == "__main__":
    unittest.main()
