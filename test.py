import unittest
from app import add, subtract, multiply, divide, exponentiate

class TestMathFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(10, 5), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-10, -5), -15)

    def test_add_positive_and_negative(self):
        self.assertEqual(add(-10, 5), -5)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-10, -5), -5)

    def test_subtract_positive_and_negative(self):
        self.assertEqual(subtract(10, -5), 15)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-10, -5), 50)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(multiply(-10, 5), -50)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 5), 2)

    def test_divide_by_zero(self):
        self.assertEqual(divide(10, 0), "Error: Division by zero!")

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -5), 2)

    def test_divide_positive_and_negative(self):
        self.assertEqual(divide(10, -5), -2)

    def test_exponentiate_positive_base_and_exponent(self):
        self.assertEqual(exponentiate(2, 3), 8)

    def test_exponentiate_negative_base_positive_exponent(self):
        self.assertEqual(exponentiate(-2, 3), -8)

    def test_exponentiate_positive_base_negative_exponent(self):
        self.assertEqual(exponentiate(2, -3), 0.125)

    def test_exponentiate_negative_base_negative_exponent(self):
        self.assertEqual(exponentiate(-2, -3), -0.125)

if __name__ == '__main__':
    unittest.main()