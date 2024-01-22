def nth_smallest(lst, n):
    # Handle invalid inputs
    if n < 1:
        raise ValueError("Invalid n value: n must be greater than or equal to 1")

    # Sort the list for efficient comparison
    lst.sort()

    # Check if the size of the list is enough for the specified nth smallest
    if len(lst) < n:
        return None

    # Return the nth smallest element
    return lst[n - 1]
