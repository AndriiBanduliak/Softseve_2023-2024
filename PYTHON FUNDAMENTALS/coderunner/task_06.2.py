def probability(lst, num):
    # Handle invalid inputs
    if not lst:
        raise ValueError("Empty list")

    # Count the number of elements greater than or equal to n
    favorable_count = len([n for n in lst if n >= num])

    # Calculate total possible outcomes (the length of the list)
    total_count = len(lst)

    # Calculate the probability as a percentage
    probability = (favorable_count / total_count) * 100.0

    # Round to one decimal place
    probability = round(probability, 1)

    return probability
