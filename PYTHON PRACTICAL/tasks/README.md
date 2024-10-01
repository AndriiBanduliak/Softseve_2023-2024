
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

