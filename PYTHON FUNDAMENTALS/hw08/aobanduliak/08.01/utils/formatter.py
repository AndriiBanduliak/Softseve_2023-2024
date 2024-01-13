def format_string(string, case="upper"):
    if case == "upper":
        return string.upper()
    elif case == "lower":
        return string.lower()
    else:
        raise ValueError("Invalid case provided. Use 'upper' or 'lower'.")
