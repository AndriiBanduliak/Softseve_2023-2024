class MyError(Exception):
    #Exception.    # enter your code
    pass

def check_positive(number):
    # enter your code
    try:
        number = float(number)
        if number < 0:
            raise MyError(f"You input negative number: {number}. Try again.")

        else:
            return f"You input positive number: {number}"

    except ValueError:
        return "Error type: ValueError!"

    except MyError as e:
        return e