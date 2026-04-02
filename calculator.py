"""
Calculator Module
Provides the core calculation functionality with validation and error handling.
"""


class Calculator:
    """A simple calculator class for performing arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator with an empty history."""
        self.history = []
    
    def calculate(self, num1, num2, operator):
        """
        Perform a calculation based on two numbers and an operator.
        
        Args:
            num1 (float): First number
            num2 (float): Second number
            operator (str): Operator (+, -, *, /)
            
        Returns:
            float: Result of the calculation
            
        Raises:
            ValueError: If operator is invalid or division by zero
            TypeError: If inputs are not numbers
        """
        # Validate inputs
        self._validate_inputs(num1, num2, operator)
        
        # Perform calculation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("Error: Cannot divide by zero!")
            result = num1 / num2
        
        # Store in history
        self.history.append({
            'operation': f"{num1} {operator} {num2}",
            'result': result
        })
        
        return result
    
    def _validate_inputs(self, num1, num2, operator):
        """
        Validate calculator inputs.
        
        Args:
            num1: First number
            num2: Second number
            operator: Operator
            
        Raises:
            TypeError: If numbers are not numeric
            ValueError: If operator is invalid
        """
        try:
            float(num1)
            float(num2)
        except (TypeError, ValueError):
            raise TypeError("Error: Inputs must be valid numbers!")
        
        valid_operators = ['+', '-', '*', '/']
        if operator not in valid_operators:
            raise ValueError(f"Error: Invalid operator '{operator}'. Valid operators are: {', '.join(valid_operators)}")
    
    def get_history(self):
        """
        Get the calculation history.
        
        Returns:
            list: List of all calculations performed
        """
        return self.history
    
    def clear_history(self):
        """Clear the calculation history."""
        self.history = []
    
    def display_history(self):
        """Display the calculation history in a formatted way."""
        if not self.history:
            print("No calculations in history yet.")
            return
        
        print("\n" + "="*50)
        print("CALCULATION HISTORY")
        print("="*50)
        for i, entry in enumerate(self.history, 1):
            print(f"{i}. {entry['operation']} = {entry['result']}")
        print("="*50 + "\n")
