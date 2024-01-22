def filter_list(lst):
    # Filter the list to remove strings
    filtered_list = [el for el in lst if isinstance(el, int)]

    # Remove duplicates from the filtered list
    filtered_list = list(set(filtered_list))

    # Ensure the original order is maintained
    filtered_list.sort(key=lambda x: lst.index(x))

    return filtered_list
