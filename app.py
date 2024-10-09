def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y (x - y)."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y (x / y)."""
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def exponentiate(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent

def main():
    print("Mathematical Functions:")
    
    # Example usage of each function
    a = 10
    b = 5
    
    print(f"Addition: {a} + {b} = {add(a, b)}")
    print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
    print(f"Division: {a} / {b} = {divide(a, b)}")
    print(f"Exponentiation: {a} ** {b} = {exponentiate(a, b)}")

if __name__ == "__main__":
    main()