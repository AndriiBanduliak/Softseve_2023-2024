import unittest


def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        if a == 0:
            raise ValueError(
                "Coefficient 'a' cannot be zero for a quadratic equation.")
        root1 = -b / (2 * a)
        return root1  # Return a single root
    else:
        if a == 0:
            raise ValueError(
                "Coefficient 'a' cannot be zero for a quadratic equation.")
        root1 = (-b + (discriminant) ** 0.5) / (2 * a)
        root2 = (-b - (discriminant) ** 0.5) / (2 * a)
        return root1, root2


class QuadraticEquationTest(unittest.TestCase):

    def test_discriminant_less_than_zero(self):
        a, b, c = 2, 3, 7
        root1 = quadratic_equation(a, b, c)
        self.assertIsNone(root1)

    def test_discriminant_greater_than_zero(self):
        a, b, c = 1, -3, 2
        root1, root2 = quadratic_equation(a, b, c)
        self.assertEqual(root1, 2.0)
        self.assertEqual(root2, 1.0)

    def test_discriminant_equal_to_zero(self):
        a, b, c = 1, -4, 4
        root1 = quadratic_equation(a, b, c)
        self.assertEqual(root1, 2.0)

    def test_a_is_zero(self):
        a, b, c = 0, 1, 2
        with self.assertRaises(ValueError):
            quadratic_equation(a, b, c)
