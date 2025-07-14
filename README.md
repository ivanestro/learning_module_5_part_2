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
