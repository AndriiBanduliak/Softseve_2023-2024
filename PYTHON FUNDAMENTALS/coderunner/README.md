# TASK 3.1

There is a single operator in Python, capable of providing the remainder of a division operation. Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.

---

# TASK 3.2

Write a function that takes an integer minutes and converts it to seconds.

---

# TASK 3.3

Create a function `addition()` that takes a number as an argument, increments the number by +1, and returns the result.

---

# TASK 3.4

Write a function that takes the base and height of a triangle and return its area. Round your answer to 2 decimal places.

---

# TASK 3.5

The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed volume of the inner sphere:

Create a function `vol_shell()` that takes r1 (R) and r2 (r4) as arguments and returns the volume of a spherical shell rounded to the nearest hundredths.

# TASK 4.1

Write a function that returns True if k^k == n for input (n, k) and return False otherwise.

The ^ operator refers to the exponentiation operation **, not the bitwise XOR operation.

---

# TASK 4.2

Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.

---

# TASK 4.3

Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

- Return a boolean value (True or False).
- Return True if the amount of x's and o's are the same.
- Return False if they aren't the same amount.
- The string can contain any character.
- When "x" and "o" are not in the string, return True.

---

# TASK 4.4

Create a function that takes a string and returns it as a positive integer.

- In that case when the string cannot be converted to a positive integer, returns the string "Not a number"

---

# TASK 4.5

Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.

---

# TASK 4.6

Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************

If the length of the number is less than 16 symbols the function returns "Invalid card"

---

# TASK 4.7

Create a function that takes a number as an argument and returns the negative of that number. Return negative numbers without any change.
# TASK 5.1

Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.

- Numbers will always be below 1024 (not including 1024).
- The strings will always go to the length at which the most left bit's value gets bigger than the number in decimal.
- If a binary conversion for 0 is attempted, return "0".

---

# TASK 5.2

Create a function that takes a string and returns the number (count) of vowels contained within it.

- a, e, i, o, u are considered vowels (not y).
- All test cases are one word and only contain letters.

---

# TASK 5.3

Create a function that returns the mean of all digits.

- The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=3).
- The mean will always be an integer.

---

# TASK 5.4

An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

- Ignore letter case (should not be case sensitive).
- All test cases contain valid one-word strings.

---

# TASK 5.5

Create a function which returns a list of booleans, from a given number. Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.

- Expect numbers with 0 and 1 only.


# TASK 6.1

You are given an unsorted list. Create a function that returns the nth smallest integer, where:
- The smallest integer is the first smallest.
- The second smallest integer is the second smallest.
- And so on.

## Notes
- n will always be >= 1.
- Each number in the array will be distinct (there will be a clear ordering).
- If the nth smallest integer is out of bounds (e.g., n > size of the list), return None.


# TASK 6.2

Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.

Notes: Percent probability of the event = 100 * (number of favorable outcomes) / (total number of possible outcomes)



---

# TASK 6.3

Given a list of numbers, create a function that returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...

---

# TASK 6.4

Create a function that takes a list of non-negative integers and strings and returns a new list without the strings.

Notes:

- Zero is a non-negative integer.
- The given list only has integers and strings.
- Numbers in the list should not repeat.
- The original order must be maintained.

---

# TASK 6.5

Create a function that takes a list and finds the list of integers that appear an odd number of times.





# TASK 8.1
## Python Module Instructions

Create a Python module named `module.py` with the following requirements:

1. When the module is run directly (`python module.py`), it should print "Hello world!" in the terminal.

2. If the module is imported, it should define a function `say_greeting(name)` that takes one argument `name` and prints "Hello {name}" in the terminal.

Ensure that your code is designed to run once in the first test case and maintains the functionality described above.

# TASK 8.2
## Water State Script Instructions

### Assume you have a Python module named `module.py` 

### Use this module in your script to print the state of the water if its temperature is determined with input from the user. We assume that the freezing point is 0 degrees and the boiling point is 100 degrees.

Do not use any function definitions or if statements in your code


# TASK 10.1

## Introduction

Create a class `BankAccount` that implements encapsulation. The class should have the following attributes:

- `account_number` (string)
- `account_holder` (string)
- `balance` (float)

## Methods

The class should have the following methods:

### `deposit(amount)`

A method that allows the account holder to deposit money into the account.

### `withdraw(amount)`

A method that allows the account holder to withdraw money from the account. If there are insufficient funds, write "Insufficient funds."

### `check_balance()`

A method that returns the current balance of the account.

## Restrictions

The class should have the following restrictions:

- `account_number` should not be accessible from outside the class.
- `balance` should not be directly accessible from outside the class; it should only be accessible through the methods `deposit()` and `withdraw()`.
- `account_holder` should be accessible from outside the class but should not be modifiable.


# TASK 10.2

## Introduction

Create a program that models a zoo. The program should have a base class `Animal` that stores the animal's name, species, and number of legs. The class should have a method `make_sound` that returns a string indicating the sound the animal makes. The `make_sound` method should be overridden in the subclasses to return a sound specific to each type of animal.

## Animal Class

The `Animal` class should have the following attributes:
- Name
- Species
- Number of Legs

And the following method:
- `make_sound`: Returns a string indicating the sound the animal makes.

## Subclasses

### Mammal

The `Mammal` class inherits from the `Animal` class and adds the following method:
- `give_birth`: Returns "Roar" for the `make_sound` method.

### Bird

The `Bird` class inherits from the `Animal` class and adds the following method:
- `lay_eggs`: Returns "Squawk" for the `make_sound` method.

### Reptile

The `Reptile` class inherits from the `Animal` class and adds the following method:
- `shed_skin`: Returns "Hiss" for the `make_sound` method.


# TASK 11.1

## Write code inside function check.

This function must check logins of some workers. We have 2 roles: there are "admin" and "employee", each login must contain role and id.

Id is any natural number. Id and role may be separated by "-" or "-id" or "id".

If function check obtains incorrect data (as an example 'abc') it needs to raise ValueError with the message "incorrect login 'abc'". Note that all data may be case-insensitive.

---

# TASK 11.2

## With help input obtain from the user his age.

Age must be a natural number.

If the user tries to input incorrect value, ask him again. If the user typed the correct age, print this value.

Do not use 'if' in your code, but you can use the already created function `check_age` for validation.

---

# TASK 11.3

## Write your code below to create a custom Error named InputError and function check.

The error must save the description of the error in the data attribute.

In the data of the error must be written:

- "Short text error" if the length of the string is less than 3,
- "Long text error" if the length of the string is more than 15,
- "Type text error" if we try to check not a string.

Your function check will be called from function test_input as shown on the screenshot.

---

# TASK 11.4

## Write the function check_odd_even (number) whose input parameter is an integer number.

The function checks whether the set number is even or odd:

- In the case of an even number, the function should display the corresponding message - "Entered number is even."
- In the case of an odd number, the function should display the corresponding message - "Entered number is odd."
- In the case of incorrect data, the function should display the message - "You entered not a number."

Note: in the function, you must use the try-except construct.

---

# TASK 11.5

## Write the function check_positive(number) whose input parameter is a number.

The function checks whether the set number is positive or negative:

- In the case of a positive number, the function should display the corresponding message - "You input a positive number: input parameter of function."
- In the case of a negative parameter, the function should return the exception of your own class MyError and display the corresponding message - "You input a negative number: input parameter of function. Try again."
- In the case of incorrect data, the function should display the message - "Error type: ValueError!"

---

# TASK 11.6

## Write the function divide(numerator, denominator) the two input parameters of which are numbers.

The function returns the result of dividing two numbers.

- In the case of correct data, the function should display the corresponding message – "Result is numerator / denominator."
- In the case of division by zero, the function should display the corresponding message – "Oops, numerator / denominator, division by zero is an error!!!"
- In the case of incorrect data, the function should display the message – "Value Error! You did not enter a number!"

Note: in the function, you must use the try-except construct.

# Task 13.1

## Celsius to Fahrenheit Conversion

Write a list comprehension function `celsius_to_fahrenheit(temps)` whose input parameter is a list of temperatures in Celsius. The function returns a new array where temperatures are converted to Fahrenheit.

Hint: The Fahrenheit to Celsius conversion formula is given by \( F = (C \times \frac{9}{5}) + 32 \).


# Task 13.2

## Problem Description

Write a function `celsius_to_fahrenheit(temps)` using the `map` function whose input parameter is a list of temperatures in Celsius. The function returns a new array where temperatures are converted to Fahrenheit.

Hint: The Fahrenheit to Celsius conversion formula is given by \( F = (C \times \frac{9}{5}) + 32 \).

# TASK 13.3

## Problem Description
Write a generator function that returns all combinations of two lists.

# TASK 13.4

## Problem Description
Create a decorator that adds a "tag" to a string. The tag will be specified as an argument to the decorator.

# TASK 13.5

## Problem Description
Write fibonacci_numbers function which returns a generator that yields the Fibonacci sequence.

# TASK 14.1

## Problem Description

You have two JSON files, `cars.json` and `cars2.json`, containing information about car models and their maximum speeds. Your task is to read both files, combine the data, and write a sorted array of cars based on their maximum speeds to a new JSON file named `result.json`.

## Instructions

1. Read data from the following input files:
   - `cars.json`: Contains an array of car models with the field `max_speed`.
   - `cars2.json`: Contains a single car object with a random `max_speed`.

2. Combine the data from both files into a single list of cars.

3. Sort the list of cars by their `max_speed` field.

4. Write the sorted array to a new JSON file named `result.json`.



# TASK 4.3.1
## Function to Count Digits

Here is a Python function that counts the number of digits in a number. It also checks if the input is a number and returns a message if it's not.


# TASK 4.3.2
This Python function takes a numeric grade (0-100) as input and returns the corresponding letter grade (A, B, C, D, or F). If the input is less than 0, it returns the message "Wrong number".

# TASK 4.3.3
# Sorting Numbers

This Python function sorts three numbers using only `if-else` statements. It takes three arguments: `num1`, `num2`, and `num3`, and prints them in ascending order.

# TASK 4.3.4
## Simple Calculator

This Python function emulates a simple calculator. It takes three parameters: `number1`, `number2`, and `operator`. The `operator` can be '+', '-', '*', or '/'. The function performs the corresponding calculation and returns the result. If the provided operator doesn't exist, it returns the message "Wrong operator".




