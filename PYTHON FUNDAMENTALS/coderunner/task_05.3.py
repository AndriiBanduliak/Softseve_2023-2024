def mean(number):
    try:
        digits = [int(digit) for digit in str(number)]
        return round(sum(digits) / len(digits))
    except ValueError:
        raise ValueError("Input must be an integer or a string containing only digits")
