def double_string(data):
    # Convert the list to a set for quick lookups
    string_set = set(data)
    counter = 0

    # Iterate over each string in the list
    for s in data:
        # Try every possible split of the string into two non-empty substrings
        for i in range(1, len(s)):  # i is the split point
            part1 = s[:i]
            part2 = s[i:]
            # If both parts exist in the set, we count this string
            if part1 in string_set and part2 in string_set:
                counter += 1
                break  # Stop checking once we find a valid split for this string

    return counter

