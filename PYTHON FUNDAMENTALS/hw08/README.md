# TASK 1

## Project Structure

The project should have the following structure:

- models
  - __init__.py
  - admin.py
  - user.py
- utils
  - __init__.py
  - formatter.py
  - logger.py
- main.py

## Steps

1. Create the structure of the Python project as shown above.
2. In the corresponding modules, create the functions `create_user`, `create_admin`, `log_in_file`, `format_string`. These functions may have an implementation like `pass`.
3. Define `__all__` in all modules so that they contain only the functions from the previous step (you can create some additional functions to test it).
4. Fill `__init__.py` files in packages so that `import*` of these packages contain only functions from the second step.


# TASK 2

Write a Python program to check the validity of a password (input from users).

## Validation Criteria

- At least 1 letter between [a-z] and 1 letter between [A-Z].
- At least 1 number between [0-9].
- At least 1 character from [$#@].
- Minimum length 6 characters.
- Maximum length 16 characters.


# TASK 3

Write a Python program to calculate the area of different shapes.

## Shapes and Formulas

- Rectangle: S = a * b
- Triangle: S = 0.5 * h * a
- Circle: S = pi * r^2

This module must be used in another module in which we ask the user the area of which figure they want to calculate.

## Note

To perform the task, you need to import the math module, and from it the pow() function and the value of variable pi, and module, which contains three functions for finding areas into the main program. The basic logic of the program is executed in the main module.
