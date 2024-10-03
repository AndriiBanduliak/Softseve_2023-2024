def studying_hours(a):
    if not a:
        return 0

    max_length = 1  # At least one element is there
    current_length = 1

    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:  # Non-decreasing condition
            current_length += 1
        else:
            # Update max length if needed
            max_length = max(max_length, current_length)
            current_length = 1  # Reset for new subarray

    # Final check at the end of the loop
    max_length = max(max_length, current_length)

    return max_length
