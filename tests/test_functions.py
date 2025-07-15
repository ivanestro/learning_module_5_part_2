"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: Ivan Estropigan
Date: 2025, 07,07 
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

import unittest
from unittest.mock import patch
from src.functions import greet_name_age, grade_outcome, prompt_name_greeting, math_operation


class TestFunctions(unittest.TestCase):
    def test_greet_name_with_all_parameters(self):
        # Arrange variables
        name = "Joe"
        age = 25
        expected = "Hello Joe, you are 25 years old!"
        # note: spelled Joe incorrectly to show failed test.

        # Act running the code what we're testing
        actual = greet_name_age(name, age)

        # Verify the output (Assert):
        # Assert compares two values 
        self.assertEqual(expected, actual)

    
    def test_grade_outcome_a_plus(self):
        # Arrange
        grade = 91
        expected = "A+"

        # Act
        actual = grade_outcome(grade)

        # Assert
        self.assertEqual(expected, actual)

    def test_grade_outcome_pass(self):
        # Arrange
        grade = 76
        low_edge = 50
        high_edge = 90
        expected = "Pass"

        # Act
        # Commented out actual = grade_outcome(grade)

        # Act and Assert, including edge cases
        self.assertEqual(expected, grade_outcome(grade))
        self.assertEqual(expected, grade_outcome(low_edge))
        self.assertEqual(expected, grade_outcome(high_edge))

    def test_grade_outcome_fail(self):
        # Arrange
        grade = 40
        high_edge = 49
        negative = -1
        expected = "Fail"

        #Act and Assert, including edge cases
        self.assertEqual(expected, grade_outcome(grade))
        self.assertEqual(expected, grade_outcome(high_edge))
        self.assertEqual(expected, grade_outcome(negative))


    def prompt_name_greeting_correct_output(self):
        # builtins.input <-- Allows us to mock input
        # builtins.print <-- Allows us to mock print
        with patch('builtins.input') as mock_input:
            # Arrange
            # The side_effect list below 'mocks' input
            # Values that are prompted for in the function:
            mock_input.side_effect = ["Joe", "Winnipeg"]
            expected = "Hello Joe, you are from Winnipeg!"

            # Act (Act within the patch context)
            actual = prompt_name_greeting()

            # Assert
            self.assertEqual(expected, actual)
    
    def test_math_operations_successful_add(self):
        # Arrange
        op1 = 10
        op2 = 20
        opt  = "+"
        expected = 30

        # Act
        actual = math_operation(op1, op2, opt)

        # Assert
        self.assertEqual(expected, actual)

    
    def test_math_operations_successful_sub(self):
        # Arrange
        op1 = 30
        op2 = 20
        opt = "-"
        expected = 10

        # Act 
        actual = math_operation(op1, op2, opt)

        # Assert
        self.assertEqual(expected, actual)

    def test_math_operation_bad_operator_raises_exception(self):
        # Arrange
        operand1 = 30
        operand2 = 20
        operator = "*"
        expected = "Invalid operation."

        # Act and Assert
        # assertRaises(ValueError) <-- Because function raises
        # ValueError when an invalid operator is provided
        with self.assertRaises(ValueError) as context:
            math_operation(operand1, operand2, operator)

        self.assertEqual(expected, str(context.exception))