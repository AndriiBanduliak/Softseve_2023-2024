import unittest


def divide(num1, num2):
    return float(num1) / num2


class DivideTest(unittest.TestCase):
    def test_success(self):
        self.assertEqual(divide(4, 2), 2.0)

    def test_success1(self):
        self.assertEqual(divide(2, 4), 0.5)

    def test_success_negative(self):
        self.assertEqual(divide(-4, 2), -2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(8, 0)
