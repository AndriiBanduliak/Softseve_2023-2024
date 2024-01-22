def divide(numerator, denominator):
    # enter your code
    try:
        result = numerator / denominator
        return f"Result is {result}"

    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"

    except TypeError:
        return "Value Error! You did not enter a number!"