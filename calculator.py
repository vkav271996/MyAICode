def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers (a - b)."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers (a / b).
    
    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


def get_number(prompt):
    """Prompt the user for a number and return it as a float."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation():
    """Prompt the user for an operation and return it."""
    operations = ['+', '-', '*', '/']
    while True:
        op = input(f"Enter operation ({'+', '-', '*', '/'}) ").strip()
        if op in operations:
            return op
        print(f"Invalid operation. Please choose from {operations}.")


def main():
    """Main function to run the calculator CLI."""
    print("\n=== Simple Calculator ===")
    
    # Get two numbers from the user
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    
    # Get the operation
    operation = get_operation()
    
    # Perform the calculation
    try:
        if operation == '+':
            result = add(num1, num2)
            op_name = "addition"
        elif operation == '-':
            result = subtract(num1, num2)
            op_name = "subtraction"
        elif operation == '*':
            result = multiply(num1, num2)
            op_name = "multiplication"
        else:  # operation == '/'
            result = divide(num1, num2)
            op_name = "division"
        
        print(f"\nResult of {op_name}: {num1} {operation} {num2} = {result}")
    except ZeroDivisionError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()