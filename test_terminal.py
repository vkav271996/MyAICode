"""Simple terminal test script."""


def get_number(prompt):
    """Prompt the user for a number and return it as a float."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """Print welcome message and calculate sum of two numbers."""
    # Print welcome message
    print("Welcome to the Terminal Calculator!")
    
    # Get two numbers from user input
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    
    # Calculate sum
    total = num1 + num2
    
    # Display result
    print(f"The sum of {num1} and {num2} is: {total}")


if __name__ == "__main__":
    main()