"""
Main Calculator Application
Provides a command-line interface for the calculator.
"""

from calculator import Calculator


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("CALCULATOR MENU")
    print("="*50)
    print("1. Perform a calculation")
    print("2. View calculation history")
    print("3. Clear history")
    print("4. Exit")
    print("="*50)


def get_number_input(prompt):
    """
    Get and validate a number input from the user.
    
    Args:
        prompt (str): The prompt to display
        
    Returns:
        float: The validated number
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number!")


def get_operator_input():
    """
    Get and validate an operator input from the user.
    
    Returns:
        str: The operator (+, -, *, /)
    """
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("Enter operator (+, -, *, /): ").strip()
        if operator in valid_operators:
            return operator
        else:
            print(f"Error: Invalid operator. Please enter one of: {', '.join(valid_operators)}")


def perform_calculation(calc):
    """
    Perform a single calculation.
    
    Args:
        calc (Calculator): The calculator instance
    """
    try:
        num1 = get_number_input("Enter first number: ")
        operator = get_operator_input()
        num2 = get_number_input("Enter second number: ")
        
        result = calc.calculate(num1, num2, operator)
        print(f"\n{'─'*50}")
        print(f"Result: {num1} {operator} {num2} = {result}")
        print(f"{'─'*50}\n")
    
    except (ValueError, TypeError) as e:
        print(f"\n✗ {e}\n")


def main():
    """Main application loop."""
    print("\n" + "="*50)
    print("WELCOME TO THE CALCULATOR APP")
    print("="*50)
    
    calc = Calculator()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            perform_calculation(calc)
        
        elif choice == '2':
            calc.display_history()
        
        elif choice == '3':
            calc.clear_history()
            print("✓ History cleared!\n")
        
        elif choice == '4':
            print("\nThank you for using the calculator. Goodbye!\n")
            break
        
        else:
            print("Error: Invalid choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
