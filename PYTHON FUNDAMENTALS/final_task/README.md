# Scientific Calculator in Python

This calculator can perform basic arithmetic operations, along with trigonometric functions, logarithms, and exponentials.

## Functions

### `button_click(char)`

This function is called whenever a button is clicked. It takes one argument, `char`, which is the character on the button that was clicked. The function adds the character to the `calc_operator` variable, which holds the current expression.

### `button_clear_all()`

This function clears the `calc_operator` variable and resets the display.

### `button_delete()`

This function deletes the last character from the `calc_operator` variable.

### `factorial(n)`

This function calculates the factorial of a non-negative integer `n`. The factorial of a number is the product of all positive integers from 1 to `n`.

### `trig_sin(n)`

This function calculates the sine of an angle `n` in degrees. The sine of an angle is the ratio of the side opposite the angle to the hypotenuse of a right triangle.

### `trig_cos(n)`

This function calculates the cosine of an angle `n` in degrees. The cosine of an angle is the ratio of the side adjacent to the angle to the hypotenuse of a right triangle.

### `trig_tan(n)`

This function calculates the tangent of an angle `n` in degrees. The tangent of an angle is the ratio of the side opposite the angle to the side adjacent to the angle.

### `trig_cot(n)`

This function calculates the cotangent of an angle `n` in degrees. The cotangent of an angle is the reciprocal of the tangent of the angle.

### `square_root()`

This function calculates the square root of a number. The square root of a number is the number that, when multiplied by itself, equals the given number.

### `third_root()`

This function calculates the cube root of a number. The cube root of a number is the number that, when multiplied by itself three times, equals the given number.

### `nth_root(n)`

This function calculates the `n`th root of a number. The `n`th root of a number is the number that, when multiplied by itself `n` times, equals the given number.

### `log_base10(n)`

This function calculates the base-10 logarithm of a number. The base-10 logarithm of a number is the power to which 10 must be raised to equal the given number.

### `log_basee(n)`

This function calculates the natural logarithm of a number. The natural logarithm of a number is the power to which e (approximately 2.71828) must be raised to equal the given number.

### `button_equal()`

This function evaluates the expression in the `calc_operator` variable and displays the result in the display.


