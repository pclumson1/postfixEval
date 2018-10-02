import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):

    def test_postfix_eval_0(self):
        self.assertAlmostEqual(postfix_eval("3 4 2 * 1 5 - 2 3 ^ ^ / +"), 3.00012207)

    def test_postfix_eval_1(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ^ + 3 -"), 83)

    def test_postfix_eval_2(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_3(self):
        try:
            postfix_eval("nope")
        except PostfixFormatException as error:
            self.assertEqual(str(error), "Invalid token")

    def test_postfix_eval_4(self):
        try:
            postfix_eval("4 +")
        except PostfixFormatException as error:
            self.assertEqual(str(error), "Insufficient operands")

    def test_postfix_eval_5(self):
        try:
            postfix_eval("1 2 3 +")
        except PostfixFormatException as error:
            self.assertEqual(str(error), "Too many operands")

    def test_postfix_eval_6(self):
        self.assertAlmostEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)

    def test_postfix_eval_7(self):
        self.assertAlmostEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)

    def test_postfix_eval_8(self):
        try:
            postfix_eval("")
        except PostfixFormatException as error:
            self.assertEqual(str(error), "Insufficient operands")

    def test_postfix_eval_9(self):
        try:
            postfix_eval("455 6 asd")
        except PostfixFormatException as error:
            self.assertEqual(str(error), "Invalid token")

    def test_postfix_eval_10(self):
        try:
            postfix_eval("455 5 6 -")
        except PostfixFormatException as error:
            self.assertEqual(str(error), "Too many operands")

    def test_postfix_eval_11(self):
        self.assertAlmostEqual(postfix_eval("5"), 5)

    def test_postfix_eval_12(self):
        self.assertAlmostEqual(postfix_eval("3 5.4 /"), 0.555555556)

    def test_postfix_eval_13(self):
        self.assertAlmostEqual(postfix_eval("4 .5 *"), 2)

    def test_postfix_eval_14(self):
        try:
            postfix_eval("4 0 /")
        except ValueError as error:
            self.assertEqual(str(error), "")

    def test_infix_to_postfix_0(self):
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"), "3 4 2 * 1 5 - 2 3 ^ ^ / +")

    def test_infix_to_postfix_1(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")

    def test_infix_to_postfix_2(self):
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_3(self):
        self.assertEqual(infix_to_postfix("6 - 3 + 2"), "6 3 - 2 +")

    def test_infix_to_postfix_4(self):
        self.assertEqual(infix_to_postfix("1 ^ 2 ^ 2"), "1 2 2 ^ ^")

    def test_infix_to_postfix_5(self):
        self.assertEqual(infix_to_postfix("1 + 2 * 3"), "1 2 3 * +")

    def test_infix_to_postfix_6(self):
        self.assertEqual(infix_to_postfix("1 ^ 2 * 5 / 2 + 6"), "1 2 ^ 5 * 2 / 6 +")

    def test_infix_to_postfix_7(self):
        self.assertEqual(infix_to_postfix("3 * 5 / 2 ^ 3"), "3 5 * 2 3 ^ /")

    def test_infix_to_postfix_8(self):
        self.assertEqual(infix_to_postfix("3 * 5 - 4 / 2 ^ 3 + 7"), "3 5 * 4 2 3 ^ / - 7 +")

    def test_infix_to_postfix_9(self):
        self.assertEqual(infix_to_postfix("5 * 3  + ( 3 / 2 )"), "5 3 * 3 2 / +")

    def test_prefix_to_postfix_0(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_1(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 4 5 - / 1 2 3"), "3 4 5 / - 1 2 / 3 - *")

    def test_prefix_to_postfix_3(self):
        self.assertEqual(prefix_to_postfix("+ + + 1 2 3 4"), "1 2 + 3 + 4 +")

    def test_prefix_to_postfix_4(self):
        self.assertEqual(prefix_to_postfix("+ + 1 * 2 3 4"), "1 2 3 * + 4 +")

    def test_prefix_to_postfix_5(self):
        self.assertEqual(prefix_to_postfix("+ + 1 * 2 3 4"), "1 2 3 * + 4 +")


if __name__ == "__main__":
    unittest.main()