
# Python Tasks

## Task 1
As input data, you have a list of strings. Write a method `double_string()` for counting the number of strings from the list, represented in the form of the concatenation of two strings from this arguments list.

## Task 2
Numbers in the Morse code have the following pattern:
- All digits consist of 5 characters.
- The number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes.
- Starting with the number 6, each dot is replaced by a dash and vice versa.

Write the function `morse_number()` for encryption of a number in a three-digit format in Morse code.

**Attention!** Do not use any collection data like lists, tuples, dictionaries for holding Morse codes.

## Task 3
The string defining the points of the quadrilateral has the next form: `#LB1:1#RB4:1#LT1:3#RT4:3`.

Where:
- LB - Left Bottom point
- LT - Left Top point
- RT - Right Top point
- RB - Right Bottom point
Numbers after letters are the coordinates of a point.

Write a function `figure_perimetr()` that calculates the perimeter of a quadrilateral.

## Task 4
As input data, you have a string that consists of words that have duplicated characters at the end of it.

All duplications may be in the next format:
- wordxxxx
- wordxyxyxy
- wordxyzxyzxyz

Using `re` module, write function `pretty_message()` that removes all duplications.

## Task 5
As input data, you have a list of strings with information about some location:

```
"id,name,population,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"
```

Using regular expression write method `max_population()` for parsing strings and get information about the location with the highest population.

## Task 6
Please specify a regular expression for matching publication formats such as "Head First. Python: PROSystem, 2021" and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022".

## Task 7
Create function `outer(name)` that returns an inner function `inner`. This inner function prints the message `Hello, <name>!`.

For example:
```python
tom = outer("tom")
tom()  # Outputs: Hello, tom!
```

## Task 8
Create function `create()` with one string argument. This function should return an anonymous function that checks if the argument of the function equals to the argument of the outer function.

For example:
```python
tom = create("pass_for_Tom")
tom("pass_for_Tom")  # Returns True
tom("pass_for_tom")  # Returns False
```

## Task 9
Create function `create_account(user_name: str, password: str, secret_words: list)` that returns an inner function `check`.

The function `check` compares the values of its arguments with the password and secret_words. The password must match completely, while secret_words may be misspelled (just one element).

The password must contain at least 6 symbols including one uppercase letter, one lowercase letter, one special character, and one number.

Otherwise, `create_account` raises a `ValueError`.

For example:
```python
tom = create_account("Tom", "Qwerty1", ["1", "word"])  # Raises ValueError
tom = create_account("Tom", "Qwerty1_", ["1", "word"])
tom("Qwerty1_",  ["1", "word"])  # Returns True
tom("Qwerty1_",  ["word"])  # Returns False
```

## Task 10
Create a function-generator `divisor()` that returns all divisors of a positive number. If there are no divisors left, the function should return `None`.

For example:
```python
three = divisor(3)
next(three)  # Outputs: 1
next(three)  # Outputs: 3
next(three)  # Outputs: None
```

## Task 11
Create a decorator `logger` that prints to the console information about the function's name and all its arguments.

Create a function `concat()` with any number of arguments that concatenates the arguments and applies the `logger` decorator.

For example:
```python
print(concat(2, 3))  # Outputs: Executing concat with arguments 2, 3... 23
print(concat('hello', 2))  # Outputs: Executing concat with arguments hello, 2... hello2
```

## Task 12
Generator function `randomWord` takes a list of words as an argument. It should return any random word from the list. Each time, words should be different until the list is exhausted.

For example:
```python
words = ['book', 'apple', 'word']
books = randomWord(words)
next(books)  # Outputs: apple
next(books)  # Outputs: book
next(books)  # Outputs: word
next(books)  # Outputs: book
```

## Task 13
Define a class `Employee`. Implement the instance attributes `firstname`, `lastname`, and `salary`. Create a static method `from_string()` which parses a string containing these attributes.

For example:
```python
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
emp1.firstname  # Outputs: "Mary"
emp1.salary  # Outputs: 60000
emp2.firstname  # Outputs: "John"
```

## Task 14
Create a `Pizza` class with the attributes `order_number` and `ingredients`. Only the ingredients will be given as input.

Hard-code some pizza flavours:

For example:
```python
p1 = Pizza(["bacon", "parmesan", "ham"])  # Order 1
p2 = Pizza.garden_feast()  # Order 2
p1.ingredients  # Outputs: ["bacon", "parmesan", "ham"]
p2.ingredients  # Outputs: ["spinach", "olives", "mushroom"]
```

## Task 15
Create a class `Employee` that takes a full name as an argument and can accept any number of keywords. The instance should have `name` and `lastname` attributes, plus any keyword attributes.

For example:
```python
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
```

## Task 16
Write a program that allows teachers to create a multiple choice test using a class `Testpaper`. The attributes should include `subject`, `markscheme`, and `pass_mark`. Create another class `Student` with the method `take_test()`.

For example:
```python
paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
student1 = Student()
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
student1.tests_taken  # Outputs: {"Maths": "Passed! (80%)"}
```

## Task 17
Create a class `Gallows` that has two instance variables: `words` (a list of words already said) and `game_over` (a boolean that becomes `True` if the game is over). Create two methods: `play()` and `restart()`.

For example:
```python
my_gallows = Gallows()
my_gallows.play('apple')  # Outputs: ['apple']
my_gallows.play('ear')  # Outputs: ['apple', 'ear']
my_gallows.play('corn')  # Outputs: "game over"
```


## Task 18: Bible Verse Filter
John wants to filter all the verses in a specific chapter in the Bible by their verse ID. The Bible has 66 books, each book has several chapters, and each chapter has many verses.

The pattern of the verse ID is `bbcccvvv`, where:
- `bb` is the Book ID (01 ≤ bb ≤ 66);
- `ccc` is the Chapter ID (001 ≤ ccc);
- `vvv` is the Verse ID (001 ≤ vvv).

John wants to find verses that belong to the specific Book and Chapter given by their IDs.


### Input:
- `scripture`: An array of strings representing verse IDs, sorted in ascending order.
- `book`: A string representing the Book ID (2 characters).
- `chapter`: A string representing the Chapter ID (3 characters).

### Output:
- A filtered array of strings containing verses from the given chapter in the given book.

---

## Task 19: Rearrange to Form a Palindrome
Given a string, check if its characters can be rearranged to form a palindrome. A palindrome is a string that reads the same from left to right and right to left.

### Example:
- `"trueistrue"` → `false`
- `"abcab"` → `true` because `"abcba"` is a palindrome.

### Input:
- `s`: A string (minimum 1 letter).

### Output:
- A boolean indicating whether the characters of the string can be rearranged to form a palindrome.

---

## Task 20: Permutation Finder
Given two permutations `p` and `q` of length `n`, find a permutation `r` such that for every `1 ≤ i ≤ n`, `q[i] = p[r[i]]`.

### Example:
- Input: `p = [5, 1, 3]`, `q = [3, 1, 5]`
- Output: `r = [3, 2, 1]`

### Input:
- `p`: An array of integers representing the first permutation.
- `q`: An array of integers representing the second permutation.

### Output:
- An array `r` representing the permutation that satisfies the condition.

---

## Task 21: Convert to Postfix Notation
Convert an expression given in standard notation (infix) to postfix notation.

The given expression can contain:
- Numbers;
- Parentheses;
- Arithmetic operators: subtraction (`-`), addition (`+`), multiplication (`*`), division (`/`), and modulo operation (`%`).

### Example:
- For `expression = ["2", "+", "3"]`, the output should be `["2", "3", "+"]`.

### Input:
- `expression`: An array of strings representing a valid expression in standard notation.

### Output:
- An array of strings representing the expression in postfix notation.

---

## Task 22: Check Array Order
Given an array of integers, determine if it is sorted in:
- "ascending" order;
- "descending" order;
- or "not sorted" at all.

### Example:
- For `a = [10, 5, 4]`, the output should be `"descending"`.
- For `a = [6, 20, 160, 420]`, the output should be `"ascending"`.
- For `a = [1, 7, 0, 4, 8, 1]`, the output should be `"not sorted"`.

### Input:
- `a`: An array of integers (all distinct, 1 < a.length < 100).

### Output:
- A string indicating whether the array is "ascending", "descending", or "not sorted".

---

## Task 23: Cipher Zeros and Points
Nicky and Dev work in a company where each member is given their income as points. On Nicky's birthday, Dev decided to gift some of his points. The number of points Dev gifts is based on the total number of visible zeros in the string representation of the `N` points he received this month.

Visible zeros are calculated as follows:
- 0, 6, and 9 contain 1 visible zero;
- 8 contains 2 visible zeros;
- Other digits do not contain visible zeros.

Nicky receives the same number of points as the visible zeros, but if the number is odd, the company adds 1 point to Nicky's gift. If the number is even and greater than 0, Nicky must give 1 point to the company.

### Example:
For `N = "565"`, the output should be `10` (binary), because Nicky receives 2 points after the adjustment.

### Input:
- `N`: A string representing the points Dev received this month (1 ≤ N ≤ 10^1000).

### Output:
- The number of points Nicky will receive as a gift, returned in binary format.

---

## Task 24: Maximum Non-decreasing Subarray Length
Nicky has an array of studying hours per day for previous exams. He wants to know the length of the maximum non-decreasing contiguous subarray to help study for his current exams.

### Example:
For `a = [2, 2, 1, 3, 4, 1]`, the answer is `3`.

### Input:
- `a`: An array of integers representing the number of hours studied each day.

### Output:
- The length of the maximum non-decreasing contiguous subarray.

## Task 25
### Problem: Valid Email Address

Write the function `valid_email(...)` to check if the input string is a valid email address or not.

- **Conditions**: 
  - An email is a string (a subset of ASCII characters) separated into two parts by the `@` symbol, a “user_info” and a “domain_info” (personal_info@domain_info).
  - In case of correct email, the function should display the corresponding message: **"Email is valid"**.
  - In case of incorrect email, the function should display the corresponding message: **"Email is not valid"**.

- **Note**: In the function, you must use the **"try-except"** construct.

---

## Task 26
### Problem: Sum of Slice in Array

Write the function `sum_slice_array(arr, first, second)` which accepts the array (list) `arr` and two numbers `first` and `second`, which represent the ordinal numbers of elements in the array that must be added. 

- For example, if 3 and 5 were entered, the 3rd and 5th elements must be added.

- **Exception Handling**: 
  - The function should raise exceptions `MyExceptions`:
    - If non-numbers or numbers less than 1 were entered.
    - If non-numbers were obtained from the array.
    - If one of the numbers or both are larger than the array length.

---

## Task 27
### Problem: Tangent of Alpha with Logging

Solve the problem of finding the tangent of the angle alpha given the sine of alpha and the cosine of alpha, and log the events in the "app.log" file.

- **Logging Levels**:
  - Log the resulting sine and cosine values at the **"info"** level.
  - Log successful calculation of the tangent at the **"debug"** level.
  - If cosine alpha = 0, log a **"warning"** with the message: **"The cosine of the angle alpha = 0. The tangent is not defined."**
  - If the tangent is not defined, log a **"critical"** with the message: **"The tangent of the angle alpha is not defined."**

- Formula: 
  - `tan(α) = sin(α) / cos(α)`

- **Note**: Do not use `print()`, `return`, or `encoding='utf-8'`.

---

# Task 28
### Problem: Solve Quadratic Equation

Write the function `solve_quadric_equation(a, b, c)` where the three input parameters `a, b, c` are numbers, and the function solves the quadratic equation:

- **Equation**: ax² + bx + c = 0

- **Conditions**:
  - If the data is correct, the function should display: **"The solutions are x1=… and x2=…"**.
  - In case of division by zero, display: **"Zero Division Error"**.
  - If data is incorrect, display: **"Could not convert string to float"**.

- **Function Examples**:
  ```python
  solve_quadric_equation(1, 5, 6)    # Output: "The solutions are x1=(-2-0j) and x2=(-3+0j)"
  solve_quadric_equation(0, 8, 1)    # Output: "Zero Division Error"
  solve_quadric_equation(1, "abc", 5) # Output: "Could not convert string to float"

# Task 29: Day of the Week
### Problem

Write a function `day_of_week(day)` where the input parameter is either a number or a string representation of a number. The function should return the corresponding day of the week if the input is in the range of 1 to 7.

- **Cases**:
  - If the input is **5**, the function should display the message: `"Friday"`.
  - If the input is not in the range 1 to 7, the function should display: `"There is no such day of the week! Please try again."`.
  - If incorrect data is provided, display: `"You did not enter a number! Please try again."`.

- **Note**: The function must use the **"try-except"** construct for error handling.



# Task 30: Calculator with Exception Handling

### Problem

We have a function `calc(a, b, op)` (as shown in the screenshot).

Write your code inside `run_calc`, where the function `calc` is called. The script must handle any kind of arguments passed to `calc`. Additionally, you need to implement proper exception handling for the following cases:

- **Exception Handling**:
  - Catch `ValueError` and print the error message.
  - Catch `TypeError` and print `"TypeError"`.
  - Catch division by zero and print `"Division by zero"`.
  - After calling `calc`, print `"End of calculation"` in all cases, even if an exception is raised.

# Task 31: Check Number Group

### Problem

Write a function `check_number_group(number)` where the input parameter is a number. The function checks whether the input number is greater than 10.

### Requirements:
- If the number is **greater than 10**, the function should display:  
  `"Number of your group (number) is valid"`.
  
- If the number is **less than or equal to 10**, the function should raise an exception of your own class `ToSmallNumberGroupError` and display:  
  `"We obtain error: Number of your group can't be less than 10"`.
  
- In the case of **incorrect data**, the function should display:  
  `"You entered incorrect data. Please try again."`.

- **Note**: The function should handle invalid inputs using the **"try-except"** construct and raise a custom exception for numbers that are too small.






# Task 32: `find(file, key)` Function

### Description:
This function parses a JSON file and returns all **unique values** of the specified key.




# Task 33: Function `parse_user`

Implement the function `parse_user(output_file, *input_files)` to create a file that contains only unique records (unique by the key "name") by merging information from all `input_files` arguments. If a user with an already existing name from a previous file is found, it should be ignored. Use pretty printing for writing users to the JSON file.

If the function cannot find the input files, log the information with an error level:


# Task 34
In user.json file we have information about users in format [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...], 

in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...]. 

Function user_with_department(csv_file, user_json, department_json) should read from json files information and create csv file in format:

header line - name, department

next lines :  <userName>, <departmentName>

If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.

Create appropriate json-schemas for user and department.

If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception  

To validate instances create function validate_json(data, schema)


# Task 35

Class Student has attributes full_name:str, avg_rank: float, courses: list
Class Group has attributes title: str, students: list.

Make both classes JSON serializable. 

Json-files represent information about student (students). 

Create methods:  

Student.from_json(json_file) that return Student instance from attributes from json-file;

Student.serialize_to_json(filename)

Group.serialize_to_json(list_of_groups, filename)

Group.create_group_from_file(students_file)

Parse given files, create instances of Student class and create instances of Group class (title for group is name of json-file without extension).


# Task 36

Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
This class should contain method serialize for serialize object to filename according to  type. 
For defining format create enum FileType with values JSON, BYTE.
Create function serialize(object, filename, filetype).
This function use SerializeManager and should serialize object to filename according to type.
For example:
if user_dict = { 'name': 'Roman', 'id': 8}
then
serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String"



## Task 37

You have to create a main course and a dessert at an Italian and a French restaurant, but you won't mix one cuisine with the other.

### Your task is:

1. Define a class `Product` with an abstract method `cook()`. This class would be the base class for the next classes:
    - `class FettuccineAlfredo` with field `name` ("Fettuccine Alfredo"), method `cook()` provides an output of the formatted string "Italian main course prepared: " and name of the dish;
    - `class Tiramisu`, with field `name` ("Tiramisu"), method `cook()` provides an output of the formatted string "Italian dessert prepared: " and name of the dish;
    - `class DuckALOrange`, with field `name` ("Duck À L'Orange"), method `cook()` provides an output of the formatted string "French main course prepared: " and name of the dish;
    - `class CremeBrulee`, with field `name` ("Crème brûlée"), method `cook()` provides an output of the formatted string "French dessert prepared: " and name of the dish.

2. Define a class `Factory` with an abstract method `get_dish()` that takes `type_of_meal` as a parameter. This class would be the base class for the classes `ItalianDishesFactory` and `FrenchDishesFactory`. The method `get_dish()` according to `type_of_meal` ("main" or "dessert") invokes the dish of appropriate cuisine.

3. Define a class `FactoryProducer` with the method `get_factory()`. The method takes the parameter `type_of_factory` and invokes the appropriate dishes factory (classes `ItalianDishesFactory` or `FrenchDishesFactory`).


## Task 38

Your task is to create an application for the departmental store. Initially, there was one and only one type of discount called the On-Sale-Discount (50%). But as time passes, the owner of the departmental store demands for including some other types of discount also for the customers.

### Solution

To solve this problem efficiently, we can use the Strategy design pattern. This pattern allows us to define a family of algorithms, encapsulate each one, and make them interchangeable. The strategy pattern lets the algorithm vary independently from clients that use it.


## Task 39

Imagine you are creating an application that shows the data about all different types of vehicles present. It takes the data from APIs of different vehicle organizations in XML format and then displays the information. But suppose at some time you want to upgrade your application with a Machine Learning algorithm that works beautifully on the data and fetches the important data only. But there is a problem, it takes data in JSON format only. It will be a really poor approach to make changes in the Machine Learning Algorithm so that it will take data in XML format.

### Solution

For solving the problem described above, you can use the Adapter Method that helps by creating an Adapter object.

#### How to Use an Adapter in Your Code

1. **Client** should make a request to the adapter by calling a method on it using the target interface.
2. Using the **Adaptee** interface, the Adapter should translate that request on the adaptee.
3. The result of the call is received by the client, and they are unaware of the Adapter’s presence.


## Task 40

Imagine we have a washing machine which can wash the clothes, rinse the clothes, and spin the clothes but all the tasks separately. We need a system that can automate the whole task without the disturbance or interference of us.

### Solution

To solve the above-described problem, we would like to use the Facade Method. It will help us to hide or abstract the complexities of the subsystems as follows