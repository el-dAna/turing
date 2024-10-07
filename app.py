import numpy as np


def greet(name):
    """
    Print a greeting message to the user.

    Parameters:
    name (str): The name of the person to greet.

    Example:
    >>> greet("Alice")
    Hello, Alice!
    """
    print(f"Hello, {name}!")


def multiply(a, b):
    """
    Multiply two numbers using 64-bit integer representation.

    This function converts the inputs to 64-bit integers and returns their product.

    Parameters:
    a (int or float): The first number to multiply.
    b (int or float): The second number to multiply.

    Returns:
    int: The product of a and b as a 64-bit integer.

    Example:
    >>> multiply(5, 3)
    15
    """
    a = np.int64(a)
    b = np.int64(b)
    return a * b


def main():
    """
    Main function to execute the greeting and multiplication operations.

    This function greets the user and performs a multiplication of two numbers,
    then prints the result.

    Example:
    >>> main()
    Hello, World!
    The multiplication result is: 15
    """
    greet("World")
    result = multiply(5, 3)
    print(
        f"The multiplication result is: {result}"
    )


if __name__ == "__main__":
    main()
