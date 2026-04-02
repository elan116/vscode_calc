"""
Unit Tests for Calculator
Tests the calculator functionality with various inputs and edge cases.
"""

import unittest
import sys
from pathlib import Path

# Add parent directory to path to import calculator
sys.path.insert(0, str(Path(__file__).parent.parent))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up a fresh calculator instance for each test."""
        self.calc = Calculator()
    
    # Basic Operations Tests
    def test_addition(self):
        """Test addition operation."""
        result = self.calc.calculate(5, 3, '+')
        self.assertEqual(result, 8)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        result = self.calc.calculate(10, 4, '-')
        self.assertEqual(result, 6)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        result = self.calc.calculate(7, 6, '*')
        self.assertEqual(result, 42)
    
    def test_division(self):
        """Test division operation."""
        result = self.calc.calculate(20, 4, '/')
        self.assertEqual(result, 5)
    
    # Edge Cases Tests
    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = self.calc.calculate(-5, -3, '+')
        self.assertEqual(result, -8)
    
    def test_decimal_numbers(self):
        """Test with decimal numbers."""
        result = self.calc.calculate(5.5, 2.5, '+')
        self.assertEqual(result, 8.0)
    
    def test_zero_addition(self):
        """Test addition with zero."""
        result = self.calc.calculate(0, 5, '+')
        self.assertEqual(result, 5)
    
    def test_zero_multiplication(self):
        """Test multiplication by zero."""
        result = self.calc.calculate(100, 0, '*')
        self.assertEqual(result, 0)
    
    # Error Handling Tests
    def test_division_by_zero(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.calculate(10, 0, '/')
    
    def test_invalid_operator(self):
        """Test that invalid operator raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.calculate(5, 3, '^')
    
    def test_invalid_number_input(self):
        """Test that invalid number input raises TypeError."""
        with self.assertRaises(TypeError):
            self.calc.calculate("abc", 5, '+')
    
    def test_invalid_number_input_second(self):
        """Test that invalid second number raises TypeError."""
        with self.assertRaises(TypeError):
            self.calc.calculate(5, "xyz", '+')
    
    # History Tests
    def test_history_recording(self):
        """Test that calculations are recorded in history."""
        self.calc.calculate(5, 3, '+')
        self.calc.calculate(10, 2, '*')
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0]['result'], 8)
        self.assertEqual(history[1]['result'], 20)
    
    def test_history_clear(self):
        """Test that history can be cleared."""
        self.calc.calculate(5, 3, '+')
        self.calc.calculate(10, 2, '*')
        self.calc.clear_history()
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 0)
    
    def test_history_operation_format(self):
        """Test that history stores operation correctly."""
        self.calc.calculate(5, 3, '+')
        
        history = self.calc.get_history()
        self.assertEqual(history[0]['operation'], '5 + 3')


if __name__ == '__main__':
    unittest.main()
