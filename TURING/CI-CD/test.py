import unittest
from unittest.mock import patch
import numpy as np
from app import greet, multiply


class TestApp(unittest.TestCase):
    """
    Test suite for the functions in the app module.

    This class contains unit tests for the `greet` and `multiply` functions
    defined in the app module. It uses the unittest framework to verify that
    these functions behave as expected.
    """

    @patch("builtins.print")
    def test_greet(self, mock_print):
        """
        Test the greet function.

        This test checks that the greet function prints the correct greeting message.
        It mocks the built-in print function to capture its output and verifies that
        it was called with the expected string.

        Expected Output:
        - When greet("World") is called, it should print "Hello, World!".
        """
        greet("World")
        mock_print.assert_called_once_with(
            "Hello, World!"
        )

    def test_multiply(self):
        """
        Test the multiply function.

        This test verifies that the multiply function correctly multiplies two numbers.
        It checks various cases including positive numbers, negative numbers,
        zero, and integer inputs. The results are compared against expected NumPy int64 values.

        Expected Cases:
        - multiply(5, 3) should return 15 (as np.int64).
        - multiply(-1, 5) should return -5 (as np.int64).
        - multiply(0, 100) should return 0 (as np.int64).
        - multiply(2, 4) should return 8 (as np.int64).
        """
        self.assertEqual(
            multiply(5, 3), np.int64(15)
        )
        self.assertEqual(
            multiply(-1, 5), np.int64(-5)
        )
        self.assertEqual(
            multiply(0, 100), np.int64(0)
        )
        self.assertEqual(
            multiply(2, 4), np.int64(8)
        )  # Testing integer input


if __name__ == "__main__":
    unittest.main()
