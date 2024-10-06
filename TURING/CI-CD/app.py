import numpy as np


def greet(name):
    print(f"Hello, {name}!")


def multiply(a, b):
    a = np.int64(a)
    b = np.int64(b)
    return a * b


def main():
    greet("World")
    result = multiply(5, 3)
    print(
        f"The multiplication result is: {result}"
    )


if __name__ == "__main__":
    main()
