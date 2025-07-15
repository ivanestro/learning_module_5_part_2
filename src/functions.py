"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: ACE Faculty
Date: {current date}
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

# Arrange
name = "Ivan"
age = 24


def greet_name_age(name: str, age: int)->str:
    """
    Description:
        Prints a greeting which includes the values of the name and age arguments.

    Args:
        name (str): The name of the person to greet.
        age (int): The age of the person to greet.
    
    Returns:
        str: A greeting including the parameter values.
    """
    return f"Hello {name}, you are {age} years old!"

def grade_outcome(grade: int) -> str:
    """
    Description:
        Provides a string outcome based on a grade argument.

    Args:
        grade (int): The earned grade.
    
    Returns:
        str: The string equivalent to the grade.
    """
    if grade > 90:
        output = "A+"

    elif grade >= 50:
        output = "Pass"

    else:
        output = "Fail"

    return output

def prompt_name_greeting() ->str:
    """
    Description:
        Prompts the user for their name and city, and returns a phrase including both values.

    Args:
        name (int): The first operand.
        city (int): The second operand.

    Returns:
        str: A greeting with both argument values included.
    """
    name = input("Enter your name: ")
    city = input("Enter your current city: ")

    return f"Your name is {name} and your current city is {city}."




def math_operation(operand1: int, operand2: int, operation: str = "+")-> float:
    """
    Description:
        Returns the result of the specified operation based on the two operands.

    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform, default = "+"

    Returns:
        result (float): result of the specified operation based on the two operands.

    Raises:
        ValueError:  "Invalid operation." When operation is not + or -.
    """

    if operation == "+":
        result = operand1 + operand2

    elif operation == "-":
        result = operand1 - operand2

    else:
        raise ValueError("Invalid operation.")

    return result

def get_square_of_number(number: int) -> int:
    """
    Description:
        Prints the square of three number to the console individually.
  
    Printing each number individually with their designed example.

    Args:
        numbers (int): The number we will square
  
    Return:
        returns the squared as an integer
    """

    return number ** 2
print(get_square_of_number(2))
print(get_square_of_number(5))
print(get_square_of_number(10))






def get_area_and_perimeter(width: float, height: float) -> tuple[float, float]:
    """
    Description:
        Returns the area and perimeter of a rectangle.
  
    Given the width and height as arguments, this function calculates the area and perimeter of the rectangle.

    Args:
        width(float): The width of a rectangle.
        height(float): The height of a rectangle.

    Returns:
        Tuple[float, float]: A tuple containing the area and perimeter of the rectangle, in that order.
    """
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

# Storing returned values in separate variables
area, perimeter = get_area_and_perimeter(5, 7)
print(f"Area: {area}, Perimeter: {perimeter}")

# Using the returned tuple directly
result = get_area_and_perimeter(3, 4)
print(f"Area: {result[0]}, Perimeter: {result[1]}")

def get_product_and_quotient(number1: float, number2: float) -> tuple[int, float]:
    """
    Description:
        Prints the quotient of two numbers to the console
    
    
    Args:
        number1 (float): number1 as float for product and quotient
        number2 (float): number2 as float for product and quotient

    Returns:
        Returns as int and float for product and quotient
    """
    product = number1 * number2
    quotient = number1 / number2
    return product, quotient

print(get_product_and_quotient(2,3))
print(get_product_and_quotient(5,2))
print(get_product_and_quotient(10,5))

#def integration() -> None:
#    """
#    #Description:
    
#    #"""
#    print(math_operation(1, 2, "+"))
#    print(prompt_name_greeting())
#    
#if __name__ == "__main__":
#    integration()

    