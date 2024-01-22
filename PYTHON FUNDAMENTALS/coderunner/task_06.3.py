def add_indexes(lst):
    # Create a new list to store the modified elements
    modified_list = []

    # Iterate through the original list
    for index, element in enumerate(lst):
        # Add the index to the element and append to the new list
        modified_element = element + index
        modified_list.append(modified_element)

    return modified_list
