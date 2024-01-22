def find_odd(lst):
    # Initialize an empty dictionary to count occurrences
    count_dict = {}

    # Iterate through the list and increment the corresponding count
    for num in lst:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    # Extract the elements with odd occurrences
    odd_occurrences = [num for num, count in count_dict.items() if count % 2 != 0]

    return odd_occurrences
