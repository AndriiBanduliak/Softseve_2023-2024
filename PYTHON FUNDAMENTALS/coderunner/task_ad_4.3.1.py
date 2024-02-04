def count_digits(number):
    if not isinstance(number, int):  # Only allow integers
        return "Wrong data type"  # Corrected message
    return len(str(abs(number)))
