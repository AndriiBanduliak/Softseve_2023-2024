def check_odd_even(number):
    try:
        if not isinstance(number, int):
            raise ValueError("You entered not a number.")
        elif number % 2 == 0:
            return "Entered number is even"
        else:
            return "Entered number is odd"
    except ValueError as e:
        return str(e)
