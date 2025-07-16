# Module 05 Demonstration Part 2

## Description
Introduction to Unit Testing

## Author

Ivan Estropigan

## Demonstration Topics

- Unit Testing
- Benefits of Unit Testing
- Directory Structure for Source Code and Tests
- Naming Conventions for Tests
- Writing and Running Tests
- Organizing Tests
- Testing Edge Cases
- Testing with Mock Objects
- Testing Exceptions

## What Is Unit Testing?

- Unit testing is a software testing methodology in which individual components or units of a software application are tested in isolation to ensure they are working correctly.

- A unit test focuses on a small part of the code, usually a single function or method and verifies that the code behaves as expected under various input conditions.

- In Python, unit tests can be written using the build-in unittest module or other third-party libraries such as pytest or nose.

- The goal is to create a series of tests that exercise differently aspects of the code and provide confidence in the code's correctness.

## Why Unit Test?

- Here are the main points we will look at:
  - Improved code quality
  - Simplified debugging
  - Better code design
  - Facilitated code refactoring
  - Enhanced collaboration
  - Continuous Integration

- **Improved Code Quality:**
  - By testing each unit of code independently, its possible to identify and fix bugs early in the development process.
  - This can help prevent bugs from propagating through the codebase and reduce the likelihood of introducing new bugs when making changes.

- **Simplified debugging:**
  - When a unit test fails, its easier to pinpoint the source of the problem since the test focuses on a small, isolated piece of code.
  - This can lead to faster debugging and problem resolution.

- **Better Code Design:**
  - Writing unit test encourages developers to create modular, loosely coupled code with well defined interfaces, generally results in a more maintainable and extensible codebase.

- **Facilitated Code Refactoring:**
  - With a comprehensive suite of unit tests, developers can confidently refactor or optimize code without fear of inadvertently breaking existing functionality.
  - If something breaks after we've made changes then the test should show it.

- **Enhanced collaboration:**
  - Unit tests can serve as documentation, clearly demonstrating the intended behavior of the code.
  - This can improve collaboration between team members and reduce misunderstandings or misinterpretations of the code.

- **Continuous Integration:**
  - Unit tests can be easily integrated into Continous Integration(CI) Pipeline, providing rapid feedback on the health of the codebase and ensuring the new changes do not introduce regressions.

## Src And Test Directories

- Organizing code into src(source code) and tests(test code) directories is a common and widely adopted practice in Python programming
  - Especially for larger projects or projects that are intended to be shared, maintained, or collaborated upon by multiple developers.

- Within the src directory is:
  - A __init__.py file (more on this below) as well a python file
  - functions.py containing some pre-coded functions.

- Within the tests directory is:
  - A __ init__.py file (more on this below) as well as a python file
  - test_functions.py containing the starting point of code which will unit test the functions in the src directory.

## __Init__.py

- __init.py files are special files that are used to indicate that the directory they are in should be considered a python package.
  - These files can be empty or can contain python code and are used to perform package initialization.
  - In this course, the files will remain empty.

- By using __init__.py files, you enable the use of absolute import paths within your project
  - This means you can import modules and objects using the full package path, such as from package.module import something

- When the __init__.py file is placed in the root directory of a python project, it signifies that the entire project directory should be treated as a python package.
  - This allows you to organize your code into multiple modules and sub packages within the project

- When placed in the src, tests, or other directories, it treats those directories as python packages and as such these packages can be imported.
  - E.g the src package and its files & functions can be imported into the test_functions.py file.
  - With __init__.py in the tests directory you have the flexibility of including subdirectories in your testing to mirror any subdirectories that may exist in the src directory.

## Unit Testing Basics

- To unit test a function, you need to determine all possible outcomes of the function.
- Open the function.py file and look at the greet_name_age function (docstring not shown):

```cs
def greet_name_age(name: str , age: int) -> str:
    return f"Hello {name}, you are {age} years old!"
```

- What is the outcome of this function?
  - A greeting is returned including a name and age.

## Structure of a test

- In python a unit test typically consists of a test class derived from unittest.TestCase
- Each method within the test class represents a single test case.
- Test case method names should start with test_ to be recognized and executed by the testing framework.

- The unittest module is a built-in python module for writing and running unit tests.
  - It provides a framework for creating test cases, test suites and test runners.
  - It does not require a pip install as it's installed with python 3.
    - A pip install is when we install extra packages/libraries.

## Imports And Filename

- Open the file called test_functions.py:
  - Review the given import statements.
  - import unittest will allow us to leverage the unittest functionality when completing the tests
  - from unittest.mock import patch will allow us to mock i/o behavior in the tests. More on this later..
  - Import the function to the unit test file:

```cs
from src. functions import greet_name_age
```

- **Note**: The filename for the test file is important.
  - The test `discovery` process that willl take place later will look for files that have a test_prefix in the file name.
  - The filename should start with the test_prefix followed by the name of the code file being tested.
  - E.G test_functions.py

## Test Class

- All test must be included in a test class
  - We haven't covered classes yet.
  - Think of them like blueprints for Things/Concepts/Objects
    - What are some data points that we would use to represent a person? a student?

- The classes created will have built within it some predefined unit test functionality that we will use.
- The class we are creating will inherit this functionality.
  - There appears to be a lot of similarities between students and persons..

- More on classes in the next module, for now define the class, and all tests cases will be within the class block:

```cs
class TestFunctions(unittest.TestCase):
```

- Class name: TestFunction - Uses TitleCase as a naming convention.
  - Also begins with the Test followed by the code module being tested within this test class (Functions)

- :Ends with a colon which signifies a block. (like if, loops, functions...)

- All tests will be written in this block (indented)

## First Test

- Define the test method header as follows:

```cs
def test_greet_name_with_all_parameters(self):
```

- self: Self refers to an instance of TestCase. Anytime we want to use the inherited TestCase functionality, we will refer to that functionality through self.

- Write test methods within the test class, using the three A's of unit testing:
  - Arrange
  - Act
  - Assert

```cs
# Arrange
[Define my variables]

#Act
[Run the code you're testing]

#Assert
[Compare expected output with output from the act phase]
```

- Set up (Arrange): Provide values for each of the two function parameters:

```cs
# Arrange
name = "Joe"
age = 25
expected = "Hello Joi, you are 25 years old!"

Note: Spelled joe incorrectly to show failed test.
```

## Running Tests

- To Run unit test there are couple of methods lets cover command line first
- To run the current test we can use the following command:
  - To use this command when working on a specific test
  - If the python terminal is not open in vs code, select terminal/New Terminal from the menu

```cs
python -m unittest -k test_greet_name_with_all_parameters
```

- In the above:
  - -m option: Indicates you are executing a module - in this case the unittest module
  - -k option: Is used to specify a pattern to match the test method names

## Review Test Results

```cs
- Hello Joi, you are 25 years old! != "Hello Joe, you are 25 years old!"

- Hello Joi, you are 25 years old!
?         ^
+ Hello Joe, you are 25 years old!
?         ^
```

- The results show that the expected does not match the actual result.
- Two possible reasons:
  - The source code has an error that has been identified by the test
  - The test contained an error (in this case the test had misspelled "Joe")

- Correct the error and re-run the test:

```cs
expected = "Hello Joe, you are 25 years old!
```

- In the terminal re-run the test  (use the up arrow to recall the last command):

```cs
python -m unittest -k test_greet_name_with_all_parameters

Ran 1 test in 0.000s

OK
```

## Review Values

- Functions can return a value using the return keyword, followed by the value to be returned.
- When a return statement is executed, the function exits, and the returned value is passed back to the caller.
- Code the following function

- Test the function:

```cs
result = math_operation(1,3, "+")
print(result)

print(math_operation(6,10, "-"))
```

- What happens if an operator other than + or - is provided to the function?
- Try calling the math_operation function with "*" operation

```cs
print(math_operation(5, 5, "*"))
# expected 25, actual 0
```

it is defaulted to subtract due because of else

## Functions.Py

- Return to functions.py 
- Review the grade_outcome function.
- What are the possible outcomes?

- Outcomes:
  1. A grade greater than 90 "A" + is returned
  2. A grade between 50 and 90 inclusive, a grade of "Pass" is returned
  3. Otherwise, a grade a "Fail" is returned

```cs
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
```

## Second Set Of Tests

1. A grade greater than 90, "A+' is returned
  - Import the grade_outcome function into test_function.py

```cs
from src. functions import greet_name_age, grade_outcome
```

- Write the first test:

```cs
def test_grade_outcome_a_plus(self):
    # Arrange
    grade = 91
    expected = "A+"
 
    # Act
    actual = grade_outcome(grade)
 
    # Assert
    self.assertEqual(expected, actual)
```

- Run the test:

```cs
python -m unittest -k test_grade_outcome_a_plus

```

- Or To Run All Test in a file you can use the following command:

## Next Test

- Define a test fora second outcome:

- A grade between 50 and 90 inclusive, a grade of 'Pass' is returned

```cs
def test_grade_outcome_pass(self):
  # Arrange 
  grade = 76 
  expected = "Pass"

  # Act
  actual = grade_outcome(grade)

  # Assert 
  self.assertEqual(expected, actual)
```

- Run the test:

```cs
python -m unittest tests/test_functions.py

Ran 3 tests in 0.000s

OK
```

## Edge Cases

- We want to make sure that the edge cases for a grade between 50 and 90 inclusive are also handled so that an invalid grade is not assigned incorrectly when on the cusp of a grade change.

- Modify the previous test as follows:

```cs
def test_grade_outcome_pass(self):
    # Arrange
    grade = 76
    low_edge = 50
    high_edge = 90
    expected = "Pass"
  
    # Act
    # COMMENT OUT actual = grade_outcome(grade)
 
    # Act and Assert, including edge cases
    self.assertEqual(expected, grade_outcome(grade))
    self.assertEqual(expected, grade_outcome(low_edge))
    self.assertEqual(expected, grade_outcome(high_edge))
```

- Run the tests and ensure it passes

## Next Test

- Define a test for the third outcome:
- Otherwise a grade of 'Fail' is returned

```cs
def test_grade_outcome_fail(self):
    # Arrange
    grade = 40
    high_edge = 49
    negative = -1
    expected = "Fail"

    # Act and Assert, including edge cases
    self.assertEqual(expected, grade_outcome(grade))
    self.assertEqual(expected, grade_outcome(high_edge))
    self.assertEqual(expected, grade_outcome(negative))
```

- Run the test and ensure it passes

## Functions.Py

- Return to functions.py
- Review the prompt_name_greting function.
- What are the possible outcomes?

```cs
def prompt_name_greeting (grade: int) -> str:
    name = input("Enter your name: ")
    city = input("Enter your current city: ")

    return f"Your name is {name} and your current city is {city}."
```

- Outcomes:
Your name is {name} and your current city is {city}.

## Third Set Of Tests

- Your name is {name} and your current city is {city}
  - Update the import Statement:

```cs
from src.functions import greet_name_age, grade_outcome, prompt_name_greeting
```

- The prompt_name_greeting function involves user interaction - the input function is used to prompt the user for a name and a city.
- Unit tests should run without the need to pause for user input.
- The user input can be 'mocked' within unit tests

## Mocking In Tests

- Mock objects are used in unit testing to simulate the behavior of real objects or dependencies that are not part of the unit being tested.

- Using mocks can help isolate the unit being tested and ensure that the test only focuses on the behavior of the unit itself.

- Python's built-in unittest.mock module provides a powerful framework for creating using mock objects.

- Note the given import statement:

```cs
from unittest.mock import patch
```

- When testing a function that uses the input function, you might want to simulate user input without acutally requiring user interaction

- By 'patching' the input function you can control what values are returned by input during the test, allowing you to test different scenarios and edge cases.
  - Aka: WE make our own input() function that will automatically return what we want it to

## Slide 38 Functions.Py

- Return to functions.py
- Review the math_operations function
- What are the possible outcomes?

```cs
def math_operation(grade: int) -> str:
    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid operation.")   
    
    return result
```

- Outcomes:
  - Successful Addition
  - Successful Subtraction
  - Successful An invalid operation
  - Successful non-numeric operand

## Fourth Set Of Tests

- Update the import statment and create the first 2 tests:

```cs
def test_math_operations_successful_add(self):
    # Arrange
    op1 = 10
    op2 = 20
    opt = "+"
    expected = 30

    # Act
    actual = math_operation(op1, op2, opt)

    # Assert
    self.assertEqual(expected, actual)


```

```cs
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

```

- Run the tests:

```cs
Ran 6 tests in 0.000s
OK
```

## Testing Exceptions

- Outcome to test:
  - An exception when an invalid operation is provided.

- The unittest.testcase class has built in functionality to confirm that under certain conditions an exception is raised.

- The `assertRaises' context manager (with clause) encloses the code that should raise the exception
  - (e.g a call to a function with invalid parameters).

- The assertRaises will confirm that an exception has been raised.

- Additionally when an exception is raised within the assertRaises context manager (with the handle `context' below): the context object can be queried for the actual exception message.

- A second assert can be used to verify the correct error message:

```cs
def test_math_operation_bad_operator_raises_exception(self):
    # Arrange
    operand1 = 30
    operand2 = 20
    operator = "*"
    expected = "Invalid operation."

    # Act and Assert
    # assertRaises(ValueError) <-- because function raises 
    # ValueError when an invalid operator is provided
    with self.assertRaises(ValueError) as context:
        math_operation(operand1, operand2, operator)
            
    self.assertEqual(expected, str(context.exception))
```

- Run the tests:

```cs
Ran 7 tests in 0.000s
OK
```

## Final Test

- Outcome to test:
  - An exception when an operand has the wrong data type.

```cs
def test_math_operation_non_numeric_operand_raises_exception(self):
    # Arrange
    operand1 = "30"  # <- non-numeric
    operand2 = 20
    operator = "-"

    # Act and Assert
    # assertRaises(ValueError) <-- because function raises 
    # ValueError when an invalid operator is provided
    with self.assertRaises(TypeError) as context:
        math_operation(operand1, operand2, operator)
            
   # In this case, we don't control the exception message
   # because it is not raised explicitly by the programmer
   # Therefore, no assert for the error message.
```

## Integration Test

- Each of the functions in function.py have been individually tested(unit tested)

- A final test may involve integrating each of the functions into a single block of code to ensure they work fine together.

- Return to functions.py

- Code the following at the bottom of the editor:

```cs
print( math_operation(1, 2, "+") )
print( prompt_name_greeting() )
```

- Run the python application (functions.py, not the test):

```cs
3
Enter your name: {your name}
Enter your current city: {your city}
Your name is {name} and your current city is {city}.
```

- Now run the Unit Test:

```cs
python -m unittest tests/test_functions.py
```

- Note  the unit test operation is being interrupted by the prompts for name and city

```cs
![alt text](image.png)
```

## Main Guard

- A main guard can be added to the source code to run the individual tests in an integrated way, but will not execute when the unit tests are run.

- A main guard, checks the context from which the code is being called.

- If the function.py file is being directly executed, then the code in the main guard will execute.

- If the code in functions.py is being indirectly executed (e.g by way of unit tests) then the code in the main guard will not execute.

## Additional Function and Unit Test Content

- The course notes provide additional content on the subjects of Functions and Unit Testing.
- This lecture focused on the techniques needed to complete Assignment 5.

## Defining Functions

A Function is a small, reusable pieces of code that performs a specific task. In Python you, create a function using the def keyword, followed by a unique identifier, parentheses, parameters and a colon. The indented lines following the colon make up the function body.

Here's a simple function example with comments to explain the code:

```python
def greet() -> None:
  """
  Description:
    Prints a greeting message to the console.

  When this function is called, print the message "Hello World" to the console.
  """

  print("Hello World")
  
  # Invoke the function by its name.

greet()
```

## Benefits Of Using Functions

Functions provide several benefits making your code more efficient, organized and easier to maintain:

- **Modularity**: Functions break complex tasks into smaller, manageable pieces, simplifying your program's structure.

- **Reusability**: Functions can be called multiple times from different parts of your code, preventing repetitive code and saving time.

- **Maintainability**: Functions improve code maintainability by making it more organized and readable. If you need to make changes, you can update the function instead of editing multiple instances of the same code.

- **Debugging**: Functions make it easier to identify and resolve bugs by dividing code into smaller units. You can test each function seperately to ensure they work correctly before integrating them.

- **Abstraction**: Functions hide the complexity of specific tasks, simplifying code comprehension. You can execute a task by calling a function without knowing its inner workings.

Understanding and effectively using functions are crucial for creating clean, efficient and maintainable python programs. Throughout the course, you'll encounter more examples and use cases for functions in python.

## Function Definition And Syntax

The syntax of a function is:

```py
def method_identifier(parameter_list, ...):
    # Implementation
```

In Python, functions are defined using the def keyword, followed by a unique function identifier, parentheses containing parameters (optional), and a colon(:).

The standard for function identifiers is to use the snake_case naming convention which means they should be lowercase and use underscores to separate words.

The function body is indented and contains the code to be executed. The body of a function is known as the function's implementation.

Here's an example of a simple function definition:

```py
def print_greeting(name: str) -> str:
  """
  Description:
    Prints a personalized greeting message to the console and returns the message.

    When called with a name, this function prints the mesage "Hello, {name}!" to the console and returns the message as a string.
  
  Args:
    name(str): The name of the person to be greeted.

  Returns:
    str: The greeting message.
  """
  greeting_message = f"Hello, {name}!"
  print(greeting_message)
  return greeting_message
```

Here's a detailed explanation of how this function works:

1. The function now accepts a single argument, **name**, with the type annotation **str**. The type annotation indicates that the **name** argument should a be string.

    ```py
    def print_greeting(name: str) -> str:
    ```

2. The updated docstring reflects the changes made to the function, explaining that it now accepts a **name** argument and returns a string.

    ```py
    """
    Description:
      Prints a personalized greeting message to the console and returns the message. When called with a name, this function prints the message "Hello, {name}!" to the console and returns the message as a string. 
    
    Args:
      name (str): The name of a person to be greeted.
    
    Returns:
      str: The greeting message.
    """
    ```

3. The function body now creates a **greeting_message** variable using an f-string which embeds the **name** argument within the message.

    ```py
    greeting_message = f"Hello, {name}"
    ```

4. The print() statement is still used to output the greeting message to the console.

   
    ```py
    print(greeting_message)
    ```
  
5. The function returns the **greeting_message** as its result.

    ```py
    return greeting_message
    ```

6. Finally, to invoke the function, call it with a name as an argument:

    ```py
    greeting = print_greeting("John")
    ```

## Function Parameters

Parameters are special variables that store the values of arguments passed along when the function is called. A function can be defined with or without parameters.

Here's an example of a function with a single parameter:

```py
def print_greeting(name: str) -> None:
  """
  Description:
    Prints a personalized greeting message to the console.

  Given a name as an argument, ths function prints a personalized greeting message to the console.

  Args:
    name (str) The name of the person to greet
  """

  print(f"Hello, {name}!")
```

Here's an example of a function with multiple parameters:

```py
def display_greet(first_name: str, last_name: str age: int) -> None:
  """
  Description:
    Prints a personalized greeting message to the console.

  Given the first name, last name, and age as arguments this function prints a personalized greeting message to the console.

  Args:
    first_name (str): The First name of the person to greet.
    last_name (str): The last name of the person to greet.
    age (int): The age of the person to greet.
  """

  print(f"Hello, {first_name} {Last_name}! You are {age} years old.")
```

The function above accepts three arguments, enclosed in parentheses ():

1. first_name with the type annotation str, indicating that this argument should be a string representing a person's first name.

    ```py
    first_name: str
    ```

2. last_name with the type annotation str, indicating that this argument should be a string representing a person's last name.

    ```py
    last_name: str
    ```

3. age with the type annotation int, indicating that this argument should be a int representing a person's age.

    ```py
    age: int
    ```

To call a function use the function name followed by the parentheses containing any required arguments. The arguments must match the order and number of parameters defined in the function.

Examples of invoking functions.

```py
# Invoking the greet() function
greet("Alice")

# Invoking the display_greet() function
display_greeting("Alice", "Johnson", 25)
display_greeting("Bob", "Smith", 25)
```

## Function Return Values

Functions can return a value using the **return** keyword, followed by the value to be returned. When a return statement is executed, the function exits, and the returned value is passed back to the caller. if a function does not have a return statement or reaches the end of the function without encountering a return statement, it will implicitly return None.

Here's an example of a function that returns the sum of two numbers:

```py
def add_numbers(first_number: int, second_number: int) -> int: 
  """
  Description:
    Returns the sum of two numbers.
  
  Given the two numbers as arguments, this function returns their sum.

  Args:
    first_number (int): The first number to add.
    second_number (int): The second number to add.

  Returns:
    int: The sum of first and second number.
  """
  sum = first_number + second_number
  return sum
```

The -> **int** following the argument list indicates the return type of the function. In this case, the function is expected to return an integer value.

```py
-> int
```

And here's an example of a function without a return statement, which implicitly returns None:

```py
def print_sum_of_numbers(first_number: int, second_number: int) -> None:
  """
  Description:
    Prints the sum of two numbers to the console.

  Given two numbers as arguments, this function prints their sum to the console.

  Args:
    first_number (int): The first number to add.
    second_number (int): The second number to add. 
  """

  sum = first_number + second_number
  print(sum)
```

## None Refresher

**None** represents the absence of a value or a null value. You'll encounter it being used in a few ways with Python:
    - Default Value for optional function parameters
    - Placeholder for uninitialized variables.
    - Default return value for functions that do not explicitly return a value.

## Programming Challenge 1

1. Define a function called get_square_of_number() that accepts one argument (a number) and returns its square.
2. Test your function by calling it with different numbers and printing the output.
Example

```py
print(get_square_of_number(2))
print(get_square_of_number(5))
print(get_square_of_number(10))
```

Output

```py
4
25
100
```

```py
def get_square_of_number(number: int) -> int:
  """
  Description:
    Prints the square of one number to the console individually.
  
  Printing each number individually with their designed example.

  Args:
    numbers (int): The number we will square
  
  Return:
    returns the squared as an integer
  """

  return = number ** 2

print(get_squared_of_number(2))
print(get_squared_of_number(5))
print(get_squared_of_number(10))
```

## Function Types And Use Case

### **Simple Functions**

Simple functions perform a single task without neeeding parameters or returning a value. They are helpful for repeated tasks in your program. Here's an example of a simple function:

```py
def print_separator() -> None:
  """
  Description:
    Prints a seperator line to the console.

  This function prints a seperator line consisting of asterisks to the console. The line has a length of 24 asterisks.
  """

  print("************************")

print("Section 1")
print_separator()

print("Section 2")
print_separator()
```

## Functions Returning Multiple Values (Tuples)

In Python, functions can return multiple values using tuples. A tuple is an ordered, unchangeable collection of elements enclosed in parentheses. When a function returns multiple values, the caller can store them in seperate variables or use them as a tuple.

Example of  function returning multiple values using a tuple:

```py
def get_area_and_perimeter(width: float, height: float) -> tuple[float, float]:
  """
  Description:
    Returns the area and perimeter ofa rectangle.
  
  Given the width and height of a as arguments, this function calculates the area and perimeter of the rectangle.

  Args:
    width(float): The width of a rectangle.
    height(float): The height of a rectangle.

  Returns:
    Tuple[float, float]: A tuple containing the area and perimeter of the rectangle, in that order.

  area = width * height
  perimeter = 2* (width + height)
  return area, perimeter
  """

# Storing returned values in separate variables
area, perimeter = get_area_and_perimeter(5,7)
print(f"Area: {area}, Perimeter: {perimeter}")

# Using the returned tuple directly
result = get_area_and_perimeter(3,4)
print(f"Area: {result[0]}, Perimeter: {result[1]}")
```

## Programming Challenge 2

Define a function called get_product_and_quotient() that accepts two arguments (two numbers) and returns their product and quotient as a tuple.

Test your function by calling it with different sets of numbers and printing the output.

Example Output:

```py
print(get_product_and_quotient(2, 3))    # Output: (6, 0.6666666666666666)
print(get_product_and_quotient(5, 2))    # Output: (10, 2.5)
print(get_product_and_quotient(10, 5))   # Output: (50, 2.0)
```

```py
def get_product_and_quotient(number1: float, number2: float) -> tuple[float, float]:
  
```

## Review Questions

1. What are the benefits of using functions in Python programs?
Code reusability, Code Readability, Easier to debug and test codes.

2. How  do you define a function in Python?
Using def keyword, by function name, parentheses a colon and indented block of code.

3. What is the purpose of parameters in a function?
The purpose of parameters is to allow functions to be receive input values.

4. How do you return a value from a function?
You'll need to use the keyword function called return.

5. What are simple function, and what are their benefits?
Simple functions takes no parameters, does not return values, performs single tasks.
    - Code readability
    - Reuseable code
    - Organization
    - Cleaner and more organized structure codes.

6. How do you return multiple values from a function using tuples?
You can return multiple tuples from a function by separating them with commas

## Parameters And Arguments

### Default Parameter Values

In Python, you can make your functions more flexible by using default parameters and keyword arguments. This allows you to provide default values for parameters and specify arguments in any order when calling a function. 

You can assign default values to parameters in your function definition. If the caller does not provide a value for a parameter, the default value is used instead.

```py
def greet(name: str, greeting: str = "Hello") -> None:
  """
  Description:
    Prints a personalized greeting message to the console.

  Given a name and an optional greeting as arguments, this function prints a personalized greeting message to the console.

  Args:
    name (str): The name of the person to greet.
    greeting (str, optional): The greeting to use. Default to "Hello".
  """
  print(f"{greeting}, {name}!")

# Uses the default greeting value
greet("Alice")

# Provides a custom greeting value
greet("Bob", "Hi")
```

```cs
Hello, Alice!
Hi, Bob
```

### Keyword Parameters

You can use keyword arguments to specify values for parameters when calling a function. This allows you to provide values for parameters in any order.

```py
def display_person_info(name: str, age: int, city: str) -> None:
  """
  Description:
    Prints a person's information to the console

  Given the name, age, city as arguments this function prints a message to the console describing the person's information.

  Args:
    name (str): The name of the person.
    age (int): The age of the person.
    city(str): The city where the person lives.
  """

  print(f"{name} is {age} years old and lives in {city}.")

display_person_info(name = "Alice", city = "New York", age = 30)

```

### Mixing Positional And Keyword Arguments

When calling a function, you can mix positional arguments and keyword arguments. However, all positional arguments must come before keyword arguments.

```py
display_person_info("Alice", city="New York", age = 30)

# Remember that when using both positional and keyword argument, you 
# Cannot provide a value for a parameter more than once.
```

## Passing Parameters By Object Reference

Understanding how Python function parameters are passed it is important for managing variables and their values in your program. Python passes parameters by object reference, which means that the reference to the object is passed, not the object itself. This has different implications for mutable and immutable objects.

## Immutable vs Mutable parameters

Immutable objects cannot be changed after they are created. When an immutable object is passed to a function, any modification to that object inside the function does not affect the original object outside the function. The following are some common immutable data are types in Python:
    - Integer
    - Float
    - String
    - Tuple
    - Boolean

Mutable objects can be changed after they are created. When a mutable object is passed to a function, any modification to that object inside the function also affects the original object outside the function. The following are some common mutable data types in Python:
    - List
    - Dictionary
    - Sets

## Effect Of Function Calls On Immutable Parameters

In this example we pass an immutable object (a string) to a function, modify it inside the function, and then print the value after the function call.

```py
def change_string(input_string: str) -> None:
  """
  Description:
    Modifies an input string by appending additional text.

  Args:
    input_string (str) The input string to be modified.
  """
  input_string += "Modified inside function"

original_string = "Original string"
change_string(original_string)
print(original_string) # Outputs "Original string"
```

As expected, the original string is not modified because strings are immutable

## Effect Of Function Calls On Mutable Parameters

In this example, we pass a mutable object (a list) to a function, modify it inside the function, and then print the value after the function call.

```py
def modify_list(input_list: list) -> None:
  """
  Description:
    Modifies input list by appending a new element.

  Args:
    input_list (list): The input list to be modified.
  """
  input_list.append("New Item")

original_list = ["Item 1", "Item 2"]
modify_list(original_list)
print(original_list)
```

Output

```py
['Item 1', 'Item 2', 'New Item']
```

## Programming Challenge

1. Define a function called calculate that takes two parameters: first_number and second_number. Set second_number to a default value of 1. Inside the function, perform additional, subtraction, multiplication, and division operations on first_number and second_number. Print the result of all four operations.

2. Test your function by calling it with different combinations of positional and keyword arguments.

Example Output:

```py
calculate(10)
print()

calculate(20, 5)
print()

calculate(first_number=15)
print()

calculate(first_number=12, second_number=3)
```

Output:

```cs
Addition: 11
Subtraction: 9
Multiplication: 10
Division: 10.0

Addition: 25
Subtraction: 15
Multiplication: 100
Division: 4.0

Addition: 16
Subtraction: 14
Multiplication: 15
Division: 15.0

Addition: 15
Subtraction: 9
Multiplication: 36
Division: 4.0
```

## Review Questions For Parameters And Arguments

1. What are default parameter values, and how do you use them in a function definition?

    Default parameters is a value that automatically used by function and it does not need to provide a passing argument.

2. What are keyword arguments, and how do they help when calling a function?

    keyword arguments lets you specify what parameter you are passing a value to. it makes the code structure clear so you know what each value means, safer to reduce coding mistakes such as missing values.

3. What is the rule for mixing positional and keyword arguments when calling a function?

    Positional argument must come first, followed by a keyword argument when calling a function.

4. How are parameters passed in Python functions?

    Parameters is passed by assignment, it assigns the arguments object to a function parameter, if the object is mutable such as a list or a dictionary they change inside the function to affect the original value, or if the object is immutable such as int, string, tuple changes inside the function to create a new object that does not affect the current values basically adding another value to the list.

5. What is the difference between immutable and mutable objects in terms of how they are affected when passed to functions?

    The difference between immutable and mutable object is:

    Immutable cannot be changed inside a function if you try to modify them a new object is created instead.

    Mutable object can be changed inside a function where the original values will not be affected but can just add things inside the existing ones. An inventory for example.

## Function Call Within Functions

### Nested Function Calls

Functions can call other functions within their bodies. This is useful for breaking down complex tasks into simpler sub-tasks, and its a common practice in programming. Each function call is independent; changes made to variables within a function do not affect other functions.

Here's an example:

```py
def greet(name: str) -> str:
  """
  Description:
    Returns a greeting message.

  Args:
    name (str): The name of the person to greet

  Returns:
    str: A greeting message.
  """
  return f"Hello, {name}!"

def greet_twice(name: str) -> None:
  """
  Description:
    Prints a greeting message twice.

  Args:
    name (str): The name of the person to greet

  print(greet(name))
  print(greet(name))
```

In the above example, the greet_twice function calls the greet function twice. This demonstrates how functions can be reused to prevent code duplication.

## The Call Stack

When a function is called, Python creates a new execution context for that call, including a new namespace for variables. This context is added to the top of the "call stack" a structure that Python uses to keep track of function calls. When the function finishes, its execution context is removed from the stack, and control returns to the previous context.

This means that variables within a function are separate from variables outside the function, evn if they have the same name. This property, known as variable scoping, prevents variables in one function from interfering with those in another.

The following is a sample example of a call stack:

```cs
Call Stack:
-----------
|         |
| func C  |
|---------|
| func B  |
|---------|
| func A  |
|---------|
|  Main   |
-----------
```

The above is a simplified, linear visualization. Each box represents a different function call, and the order of the boxes represents the order of the function calls (from bottom to top). You can replace "funcA", "funcB", etc. with the actual names of your function. The 'Main' refers to the main program context. The box at the top represents the function currently being executed. When that function completes, it is removed from the "stack", and the next function down becomes the current function.

## Returning A Function Call

Functions can also return the result of calling another function. This is a powerful technique that allows functions to be composed together to perform more complex operations.

Here's an example:

```py
def square(number: int) -> int:
    """Returns the square of a number.

    Args:
        number (int): The number to square.

    Returns:
        int: The square of the number.
    """

    return number ** 2

def square_sum(first_number: int, second_number: int) -> int:
    """Returns the sum of the squares of two numbers.

    Args:
        first_number (int): The first number.
        second_number (int): The second number.

    Returns:
        int: The sum of the squares of the numbers.
    """

    return square(first_number) + square(second_number)
```

In the above example, the square_sum function calls the square function twice, adding together the result

## Review Questions Function Calls Within Functions

1. How can functions call other functions within their bodies?
    To call other function within their bodies to to use the name of the function they want to call using parentheses example 

    ```py
        def greet():
          print("Hello")

        def introduce():
          greet()
          print("Welcome to the program")

    introduce()
    ```

2. What is the call stack and how does it relate to function execution?
    Call stack is a data structure to keep track of functions during execution of a program.

    It Controls the order that function is run, pause or return to make sure that your code runs smoothly.

3. What does it mean to return a function call from another function?
    You call a function to another function and return the result of that first function call which then translates to your second function and outer of it will call the result example.

```py
    def add(a, b):
      return a + b

    def calculate():
    return add(3, 4)  # return the result of calling add(3, 4)

result = calculate()
print(result)  # Output: 7
```

## FINISH THE REST

Reading Them And Finish The Rest Later.

- Scope
- Function Documentation
- Unit Testing
- Unit Testing Standards & Best Practices
- Unit Testing Techniques
