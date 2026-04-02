# Calculator Application

A simple, user-friendly command-line calculator built with Python.

## Features

✅ **Basic Arithmetic Operations**
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

✅ **Input Validation**
- Validates numeric inputs
- Validates operator selection
- Handles invalid entries gracefully

✅ **Error Handling**
- Prevents division by zero
- User-friendly error messages
- Exception handling for all edge cases

✅ **Calculation History**
- Tracks all calculations performed
- View history anytime
- Clear history when needed

✅ **User-Friendly CLI Interface**
- Interactive menu system
- Clear prompts and feedback
- Formatted output with visual separators

## Project Structure

```
calculator_project/
├── calculator.py          # Core calculator logic
├── main.py               # CLI interface
├── requirements.txt      # Project dependencies
├── README.md            # This file
└── tests/
    └── test_calculator.py # Unit tests
```

## Installation

1. **Prerequisites**: Python 3.6 or higher

2. **Clone or download this project**

3. **No external dependencies needed** - The calculator uses only Python standard library

## Usage

### Running the Calculator

```bash
python main.py
```

### Menu Options

Once the calculator is running, you'll see this menu:

```
1. Perform a calculation
2. View calculation history
3. Clear history
4. Exit
```

### Example Workflow

```
Welcome to the Calculator - Please select an option:
1. Perform a calculation
2. View calculation history
3. Clear history
4. Exit

Enter your choice (1-4): 1

Enter first number: 10
Enter operator (+, -, *, /): +
Enter second number: 5

──────────────────────────────────────────────────
Result: 10.0 + 5.0 = 15.0
──────────────────────────────────────────────────
```

## Running Tests

Run the unit tests to verify everything works correctly:

```bash
python -m unittest tests.test_calculator
```

Or run a specific test:

```bash
python -m unittest tests.test_calculator.TestCalculator.test_addition
```

## Test Coverage

The test suite includes:
- ✓ Basic arithmetic operations (addition, subtraction, multiplication, division)
- ✓ Edge cases (negative numbers, decimals, zero)
- ✓ Error handling (division by zero, invalid operators, invalid inputs)
- ✓ History functionality (recording, clearing, formatting)

## Code Structure

### calculator.py

The `Calculator` class provides:
- `calculate(num1, num2, operator)` - Performs calculations
- `get_history()` - Returns calculation history
- `clear_history()` - Clears all records
- `display_history()` - Displays history in formatted output

### main.py

The CLI interface provides:
- Interactive menu system
- Input validation and error handling
- User-friendly prompts and feedback
- History display and management

## Error Handling Examples

The calculator handles:
- **Division by Zero**: "Error: Cannot divide by zero!"
- **Invalid Operator**: "Error: Invalid operator. Valid operators are: +, -, *, /"
- **Invalid Number**: "Error: Please enter a valid number!"
- **Invalid Menu Choice**: "Error: Invalid choice. Please enter 1, 2, 3, or 4."

## Example Calculations

```
10 + 5 = 15
20 - 8 = 12
7 * 6 = 42
100 / 4 = 25
-5 + 3 = -2
5.5 * 2 = 11
```

## Future Enhancements

Possible improvements:
- [ ] Add advanced operations (square root, power, percentage)
- [ ] Create a graphical user interface (GUI)
- [ ] Save history to a file
- [ ] Add keyboard shortcuts
- [ ] Memory functions (M+, M-, MR, MC)
- [ ] Different calculation modes (standard, scientific)

## Notes

- All calculations are performed with floating-point precision
- History is stored during the session (lost when program exits)
- The calculator supports both integers and decimal numbers

## License

This is an educational project - feel free to use and modify as needed.

## Support

For issues or questions:
1. Review the test cases in `tests/test_calculator.py`
2. Check the docstrings in `calculator.py` and `main.py`
3. Verify all inputs are valid (proper numbers and operators)
